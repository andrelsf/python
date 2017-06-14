#!/usr/bin/env python3
"""
Author.: Andre L S Ferreira
Date...: 25/05/2017
Purpose: Implementar regras de firewall iptables com a linguagem python.
Name...: firewall.py

"""
import os

iptables = ('/usr/bin/iptables ')

modprobe = ('/usr/sbin/modeprobe ')

interfaces = {'local_int': [('eth1', 'eth2')],
        'ext_int': [('eth0')]}

tables = ('-t filter ', '-t nat ', '-t mangle ')

chains = {'filter': [('INPUT', 'OUTPUT', 'FORWARD')],
        'nat': [('PREROUTING', 'INPUT', 'OUTPUT', 'POSTROUTING')],
        'mangle': [('PREROUTING', 'INPUT', 'OUTPUT', 'FORWARD', 'POSTROUTING')]}

policies = { '-P INPUT ': 'DROP',
        '-P OUTPUT ': 'ACCEPT',
        '-P FORWARD ': "DROP" }

"""Executa comandos"""
def exec_cmd(cmd):
    try:
        os.system(cmd)
    except:
        print("Command not found.")

def charge_modules():
    try:
        with open('modules', 'r') as obj_mod:
            modules = obj_mod.readlines()
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    else:
        for module in modules:
            modp_cmd = modprobe + module
            exec_cmd(modp_cmd.rstrip())

"""Aplica Políticas"""
def apply_policies():
    for key, value in policies.items():
        cmd = iptables + key + value
        exec_cmd(cmd)

def fxz_rules():
    i = int(0)
    while i < len(tables): 
        t_flush = iptables + tables[i] + "-F"
        t_xchain = iptalbes + tables[i] + "-X"
        t_zcount = itpables + tables[i] + "-Z"
        exec_cmd(t_flush)
        exec_cmd(t_xchain)
        exec_cmd(t_zcount)
        i += 1

def main():
    #charge_modules()
    #flush_rules()
    #apply_policies()


if __name__ == "__main__":
    main()

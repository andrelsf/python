#coding: utf-8
"""
Faz a leitura do arquivo passwd

"""
pathfile = '/etc/passwd'

with open(pathfile, 'r') as passwd:
    for line in passwd:
        if 'bash' in line:
            print(line.rstrip())


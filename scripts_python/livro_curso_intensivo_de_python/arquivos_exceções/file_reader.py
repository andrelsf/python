#coding: utf-8
"""Abre o arquivo, lê os dados e exibe o conteudo na tela"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("")

"""Path em uma variavel"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("")
"""Criando uma lista de linhas de um arquivo"""
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

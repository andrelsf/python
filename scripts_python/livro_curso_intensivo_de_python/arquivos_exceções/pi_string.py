#coding: utf-8
"""Trabalhando com o conteudo de um arquivo"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print("PIString: " + pi_string)
print("Tamanho.: " + str(len(pi_string)))

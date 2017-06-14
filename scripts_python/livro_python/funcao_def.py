#
# Exemplo de FUNCAO: COMANDO DEF
#
#coding: utf-8

def sum(a, b):
    return a + b

def input_a():
    a = int(input("A: "))
    return a

def input_b():
    b = int(input("B: "))
    return b

c = sum(input_a, input_b)

print("Soma de A + B: ", c)

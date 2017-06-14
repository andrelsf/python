#
#
# Escreva um algoritmo que receba dez números do usuário e imprima o quadrado de cada número.
#
#coding: utf-8

x = 1
while x <= 10:
    num = float(input("Entre com {}º valor: ".format(x)))
    print(num * num)

    x = x + 1

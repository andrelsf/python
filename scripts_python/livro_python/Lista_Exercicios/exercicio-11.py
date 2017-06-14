#
#
# Escreva um algoritmo que receba dez números do usuário e imprima a metade de cada número.
#
#coding: utf-8

x = 1
while x <= 10:
    num = float(input("Digite o {n}º valor: ".format(n=x)))
    print(num/2)

    x = x + 1

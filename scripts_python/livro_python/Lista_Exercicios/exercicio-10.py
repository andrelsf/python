#
#
# Escreva um algoritmo que imprima todos os números ímpares do intervalo fechado de 1 a 100
#
#coding: utf-8

x = 1
while x <= 100:
    if(x % 2 != 0):
        print(x, end=' - ')

    x = x + 1

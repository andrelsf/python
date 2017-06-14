#!/usr/bin/env python3
#
# Elabore um algoritmo que leia dez numeros inteiros e imprima o maior e menor numero da lista.
#
# -*- coding: utf-8 -*-

maior = 0
menor = 0

x = 1
z = 1
while x <= 10:
    num = int(input("Entre com {}º valor: ".format(x)))
    if x == 1:
        maior = num
        menor = num
    elif maior < num:
        menor = maior
        maior = num
    x = x + 1
print("Maior: ", maior)
print("Menor: ", menor)

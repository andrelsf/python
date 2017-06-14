#!/usr/bin/env python3
#
# Elabore um algoritmo que leia dez numeros inteiros e imprima o maior e o segundo maior numero da lista.
#
# -*- coding: utf-8 -*-

maior = 0
smaior = 0

x = 1
while x <= 10:
    num = int(input("Entr com {}º valor: ".format(x)))
    if x == 1:
        maior = num
        smaior = num
    elif maior < num:
        smaior = maior
        maior = num
    x = x + 1
print("Maior........: ", maior)
print("Segundo Maior: ", smaior)

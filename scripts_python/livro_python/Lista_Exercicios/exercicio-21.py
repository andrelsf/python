#!/usr/bin/env python3
#
# Crie um algoritmo que leia um número (NUM) e depois leia (NUM) numeros inteiros e imprima o maior deles.
# Suponha que todos os numeros lidos serão positivos.
#
# -*- coding: utf-8 -*-

num1 = int(input("Entre com numero inteiro: "))
num2 = int(input("Entre com numero inteiro: "))

if num1 > num2:
    print("Maior NUM(1): ", num1)
elif num2 > num1:
    print("Maior NUM(2): ", num2)
else:
    print("")

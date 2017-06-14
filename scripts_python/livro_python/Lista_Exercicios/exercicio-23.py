#!/usr/bin/env python3
#
# Elabore um algoritmo que leia um numero(NUM) e depois leia NUM numero inteiro e imprima o menor deles.
#
# -*- coding: utf-8 -*-
num1 = 0
num2 = 0

num1 = int(input("Entre com numero: "))
num2 = int(input("Entre com numero: "))

if num1>0 and num2 > 0:
    if num1 < num2:
        print("Menor NUM1: ", num1)
    else:
        print("Menor NUM2: ", num2)
else:
    print("Algum dos numeros não foi preechidos.")

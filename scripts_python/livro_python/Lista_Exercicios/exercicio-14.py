#!/usr/bin/env python3
#
#
# Escreva um algoritmo que receba quinze números de usuário e imprima a raiz quadrada de cada número.
# 
# -*- coding: utf-8 -*-
import math

x = 1
while x <= 15:
    num = float(input("Entre com {}º valor: ".format(x)))
    print(math.sqrt(num))
    x = x + 1

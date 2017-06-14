#!/usr/bin/env python3
#
#
# Escreva um algoritmo que receba oito números do usuário e imprima o logaritmo de cada um deles na base 10.
#
# -*- coding: utf-8 -*-
import math

x = 1
while x <= 8:
    num = float(input("Entre com {}º valor: ".format(x)))
    print(math.log10(num))

    x = x + 1

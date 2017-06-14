#!/usr/bin/env python3
#
# Crie um algoritmo que imprima todos os números de 1 até 100, inclusive a soma de todos eles. 
# 
# -*- coding: utf-8 -*-

x = 1
while x <= 100:
    soma = x + x
    print("{} - Soma: ".format(x), soma)
    x = x + 1

#!/usr/bin/env python3
#
# Crie um algoritmo que imprima todos os numeros de 1 ate 100, inclusive, e a soma da metade desses numeros.
#
# -*- coding: utf-8 -*-

x = 1
while x <= 100:
    soma = (x + (x/2))
    print("{} - Soma: ".format(x), '{0:,.2f}'.format(soma))
    x = x + 1

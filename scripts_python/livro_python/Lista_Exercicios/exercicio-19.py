#!/usr/bin/env python3
#
# Criar um algoritmo que imprima todos os numeros de 1 ate 100, inclusive, e a soma do cubo desses numeros.
#
# -*- coding: utf-8 -*-

import math

x = 1
while x <= 100:
    soma = (x + (math.pow(x,3)))
    print("{} - Soma: ".format(x), '{0:,.2f}'.format(soma))
    x = x + 1

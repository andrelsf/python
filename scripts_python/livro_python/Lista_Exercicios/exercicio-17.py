#!/usr/bin/env python3
#
# Escreva um algoritmo que imprima todos os numeros de 1 ate 100, inclusive a soma do quadrado desses números.
#
# -*- coding: utf-8 -*-
import math
#from decimal import *

x = 1
while x <= 100:
    soma = x + (math.sqrt(x))
    print("{} - Soma: ".format(x), '{0:,.2f}'.format(soma))
    #print("{} - Soma: ".format(x), Decimal(soma))
    x = x + 1

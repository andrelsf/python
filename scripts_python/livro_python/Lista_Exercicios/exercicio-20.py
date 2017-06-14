#!/usr/bin/env python3
#
# Escreva um algoritmo que imprima todos os numeros de 1 ate 100, inclusive, e a media de todos eles.
#
# -*- coding: utf-8 -*-

x = 1
while x <= 100:
    media = x/100;
    print("{} - Media: ".format(x), '{0:,.2f}'.format(media))
    x = x + 1

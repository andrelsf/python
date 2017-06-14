#!/usr/bin/env python3
#
# Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares
# no intervalo aberto e seu somatório. Suponha que os dados digitados são para um intervalo crescente, ou seja
# o primeiro valor é menor que o segundo.
#
# -*- coding: utf-8 -*-

maior = 0
menor = 0

x = 1
while x <= 5:
    num = int(input("Entre com {}º valor: "))
    if x == 1:
        maior = num
    elif maior < num:
        menor = maior
        maior = num
    x = x + 1


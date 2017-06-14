#
# Exemplo de FUNCAO DEF
#
#coding: utf-8 

def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)

salario = int(input("Salario: R$"))

print("Desconto Salarial: R$", salario_descontado_imposto(salario))

#
# Exemplo de While com break
#
salario = int(input('Salario: R$'))
imposto = 27.

while imposto > 0:
    imposto = input('Digite o imposto ou (s) para sair: ')
    if not imposto:
        imposto = 27.
    elif imposto == 's' or imposto == 'S':
        break
    else:
        imposto = float(imposto)
    print("Valor real: R${0}".format(salario - (salario * (imposto * 0.01))))


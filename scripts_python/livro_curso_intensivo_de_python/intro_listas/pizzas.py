#
#
# Pizzas 4.1
#
#coding: utf-8

pizzas = []
qtde_pizzas = int(input("Quantas pizzas deseja pedir: "))

x = 1
while x <= qtde_pizzas:
    pizzas.append(input("Qual pizza? "))
    x += 1

print("\nPizzas pedidas:")
for pizza in pizzas:
    print("* Gosto de pizza de " + pizza.title())

print("Eu realmente adoro pizza.")


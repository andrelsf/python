#
#
#
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# Ordem alfabetica temporariamente preservando o estado anterior da lista
print("SORTED: " + str(sorted(cars)))

# Ordem alfabetica de forma permanente
cars.sort()
print("\nSORT: " + str(cars))

# Ordem inversa da lista
cars.reverse()
print("\nReverse: " + str(cars))

# Ordem alfabetica reversa de forma permanente
cars.sort(reverse=True)
print("\nSORT Reverse: " + str(cars))

# Obtendo o tamanho de uma lista
print("\nO tamanho da lista de carros: " + str(len(cars)) + "\n")

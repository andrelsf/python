#
# Modificando elementos da lista
#

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Adiciona à lista no final
motorcycles.append('ducati')

# Modifica elemento da lista 
#motorcycles[0] = 'ducati'

# Criando uma lista vazia e adicionando conforme necessario (append)
marcas = []
marcas.append('Honda')
marcas.append('Yamaha')
marcas.append('Suzuki')
marcas.append('Ducati')

# Inserindo elemento em uma lista na possição especifica (insert)
motorcycles.insert(0, 'Harley-Davidson')
motorcycles.insert(1, 'BMW')
marcas.insert(0, 'harley-davidson')
marcas.insert(1, 'BMW')

# Removendo um elemento usando a instrução (del)
del motorcycles[0]
del motorcycles[1]
del marcas[1]

print(motorcycles)
print(marcas)
print("")

# O método pop() remove o ultimo item de uma lista e permite o trabalho com esse item depois da remoção
popped_motorcycles = motorcycles.pop()
print("Lista Motorcycles: " + str(motorcycles))
print("Lista Popped.....: " + str(popped_motorcycles))

popped_marcas = marcas.pop()
print("\nLista Marcas: " + str(marcas))
print("Lista Popped..: " + str(popped_marcas))

# Removendo itens de qualquer posição da lista (pop())
first_owned = motorcycles.pop(0)
print('A primeira motocicleta que eu ganhei foi uma ' + first_owned.title() + '.')

# Removendo um item de acordo com o valor
print(marcas)
too_expensive = 'Honda'
marcas.remove(too_expensive)
print(marcas)
print("\nA " + too_expensive.title() + " é muito cara para mim.")

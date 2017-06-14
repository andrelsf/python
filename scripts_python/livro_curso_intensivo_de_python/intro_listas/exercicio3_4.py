#
#
#
print("\nLista de Convidados Jantar")
nomes = []
nomes.append(input("Nome: "))
nomes.append(input("Nome: "))
nomes.append(input("Nome: "))

popped_nomes = nomes.pop(0)
print("\nO " + popped_nomes.title() + " não poderá participar do jantar.")

nomes.append(input("Convidar outra pessoa: "))

print("\nOpá temos mais 3 espaço a mesa, vamos convidade mais")

nomes.insert(0, input("Nome: "))
nomes.insert(0, input("Nome; "))
nomes.append(input("Nome: "))

print("\nTemos " + str(len(nomes)) + " convidados a nossa lista de convidados.\n")

x = 0
nomes.sort()
while x < len(nomes):
    print("\t * " + nomes[x].title())
    x += 1

print("")

x = 0
while x < nomes.__len__():
    print("Bem vindo " + nomes[x].title() + " você foi convidado para jantar conosco.")
    x += 1



#
#
# 2.3 Mensagem Pessoal: Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a esta pessoa.
# Sua mensagem deve ser simples, como "Aló Eric, voce gostaria de aprender um pouco de python hoje?".
#
name = "Andre"
print("Ola "+ name + " voce gostaria de trabalhar na SOLUTI.")

resposta = input("Entre com sim ou não!")

if resposta == "sim":
    print("Bem vindo a SOLUTI " + name)
else:
    print("Deus tem o melhor para vc " + name)

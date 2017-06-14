#coding: utf-8
"""
Escrevendo dados em um arquivo vazio
"""
#message_write = input("Message: ")

filename = 'programming.txt'

"""
Modo leitura (r)
Modo escrita (w)
Modo de concatenação ('a')
Modo que permite ler e esquever ('r+')
Se omitido o argumento opera em modo de leitura

Caso o arquivo não exista o metódo open() cria o arquivo!
"""
with open(filename, 'a') as file_object:
    #file_object.write(message_write)
    while True:
        message = input("Message: ")
        if message.lower() == 's':
            break
        else:
            file_object.write(message.rstrip() + "\n")

#with open(filename, 'a') as file_object:
#    file_object.write("I also love finding meaning in large datasets.\n")
#    file_object.write("I love creating apps that can run in a browser.\n")

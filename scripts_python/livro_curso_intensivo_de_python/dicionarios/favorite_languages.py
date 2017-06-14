#coding: utf-8
favorite_languages = {
        'jen': 'python',
        'andrews': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'java',
        'chris': 'java'
        }

print("Andrews favorite language is " +
        favorite_languages['andrews'].title() + ".")

# Percorrendo todos os itens chave-valor de um dicionario
for name, language in favorite_languages.items():
    print(name.title() + 
            "'s favorite language is " + 
            language.title() + ".")

# Percorrendo todas as chaves de um dicionario com um laço
print("")
for name in favorite_languages.keys():
    print(name.title())

# Trabalhando com if ao percorrer dentro do laço
print("")
friends = ['edward', 'phil']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() +
                ", I see your favorite language is " +
                favorite_languages[name].title() + "!")

# Verificando se uma pessoa participou da enquete
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")

# Percorrendo as chaves de um dicionario em ordem usando um laço
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Percorrendo todos os valores de um dicionário com um laço
# O set() usado para remover itens duplicados
print("\nThe following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

# Uma lista em um dicionario
favorite_languages_2 = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell']
        }

for name, languages in favorite_languages_2.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())



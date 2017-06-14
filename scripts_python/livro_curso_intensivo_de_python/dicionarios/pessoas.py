#coding: utf-8
pessoa = {
        'first_name': 'Andre',
        'last_name': 'Ferreira',
        'age': 32,
        'city': 'goiânia'
        }

print(pessoa['first_name'].title() + 
        " " + pessoa['last_name'].title() +
        " possui " + str(pessoa['age']) +
        " anos e reside em " + pessoa['city'].title())

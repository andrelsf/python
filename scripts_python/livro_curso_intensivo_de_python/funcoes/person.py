#
# Devolvendo um dicionario
#
#coding: utf-8

def build_person(first_name, last_name, age=''):
    """Devolve um dicionario com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")
iage = input("Your age: ") 

fullname = build_person(firstname, lastname, iage)

print(fullname)

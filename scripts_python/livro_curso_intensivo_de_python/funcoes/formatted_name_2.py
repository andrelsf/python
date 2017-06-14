#
# Deixando um argumento opcional
#
#coding: utf-8
def get_formatted_name(first_name, last_name, middle_name=''):
    """ Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
fullname = get_formatted_name(firstname, lastname)
print(fullname)

firstname = input("Enter First Name: ")
middlename = input("Enter Middle Name: ")
lastname = input("Enter Last Name: ")

fullname = get_formatted_name(firstname, middlename, lastname)
print(fullname)


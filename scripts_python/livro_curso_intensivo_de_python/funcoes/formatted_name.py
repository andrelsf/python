#coding: utf-8

def get_formatted_name(first_name, last_name):
    """ Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

firstname = input("Enter first name: ")
lastname = input("Enter last name.: ")

fullname = get_formatted_name(firstname, lastname)
print(fullname)

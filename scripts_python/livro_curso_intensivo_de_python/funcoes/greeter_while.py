#
#
#coding: utf-8

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

def exit_program():
    print("Program Finalized.")
    break

while True:
    print("\nPlease tell me your name: ")
    f_name = input("First Name: ")
    if f_name == 'q':
        exit_program()
    l_name = input("Last Name.: ")
    if l_name == 'q':
        exit_program()

    formatted_name = get_formatted_name(f_name, l_name)
    print("\n Hello, " + formatted_name + "!")


#coding: utf-8
"""Passando uma lista para uma função"""

def greet_users(names):
    """Exibe uma simples saudação a cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

#def exit_program():
#    print("Program finalized.")
#    break

usernames = []
while True:
    name = input("Enter Name or 'q' to exit: ")
    if name.lower() == 'q':
        break
    else:
        usernames.append(name)

greet_users(usernames)

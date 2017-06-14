#coding: utf-8
#def greet_user():
#    """Exibe uma saudação"""
#    print("Hello!")

def greet_user(username):
    print("Hello, " + username.title())

username = input("Enter your name: ")
greet_user(username)

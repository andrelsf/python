#coding: utf-8

class User():
    def __init__(self, first_name, last_name, 
            location, user_name):
        """ Inicializa os atribuitos da classe """
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.user_name = user_name

    def describe_user(self):
        print("Informações do Usuário: \n" +
                "Username: " + self.user_name + "\n" +
                "Full name: " + self.first_name.title() + 
                " " + self.last_name.title() + "\n" +
                "Location: " + self.location.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " welcome.\n")

user_1 = User('andre', 'ferreira', 'TI', 'aferreira')
user_2 = User('chris', 'rezende', 'Comercial', 'crezende')
user_3 = User('beatriz', 'souza', 'Maternal', 'bsouza')

list_users = [user_1, user_2, user_3]
for user in list_users:
    user.describe_user()
    user.greet_user()

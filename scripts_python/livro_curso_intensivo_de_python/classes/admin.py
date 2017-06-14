#coding: utf-8

class User():

    def __init__(self, first_name, last_name, 
            location, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.user_name = user_name

    def get_info(self):
        print("Informações: " + "\n\tUsername: " + self.user_name +
                "\n\tName: " + self.first_name.title() + 
                " " + self.last_name.title() + 
                "\n\tLocation: " + self.location)



class Admin(User):
    def __init__(self, first_name, last_name,
            location, user_name):
        super().__init__(first_name, last_name,
                location, user_name)
        self.privileges = ['can add post', 'can delete post', 'can blocker user']

    def show_privileges(self):
        print("Username: " + self.user_name + 
                "\nPrivileges: ") 
        for p in self.privileges:
            print(" - " + p)




admin = Admin('andre', 'ferreira', 'TI', 'aferreira')
user_info = admin.get_info()
print(user_info)
show_priv = admin.show_privileges()
print(show_priv)

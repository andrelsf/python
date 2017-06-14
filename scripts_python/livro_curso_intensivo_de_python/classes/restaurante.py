#coding: utf-8

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """ Inicializa os atribuitos """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + 
                ". Your kind of cuisine is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() +
                " is open.")

my_restaurant = Restaurant('Brioshi', 'Italian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

"""
Player Model

"""


# Define user class
class User (object):
    # init city with its name and starting city

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.inventory = {}

    # move player to a new city object
    def move_city(self, new_city):
        self.city = new_city

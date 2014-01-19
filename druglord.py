#!/usr/bin/python
# -*- coding: utf-8 -*-

#Define city classes

import gc

DEFAULT_DAYS = 3

class City (object):
	def __init__ (self, name):
		self.name = name


#Define user classes
class User (object):
	def __init__(self, name, city):
		self.name = name
		self.city = city

	def get_city(self):
		print self.city.name

	def move_city(self, new_city):
		self.city = new_city

def game_welcome():
	print "Welcome to Drug Lord"
	print "Choose an option:"
	print "1) New Game"
	print "2) Exit"

def game_actions():
	print "1) Move City"
	print "2) Exit"

def get_all_cities():
	for obj in gc.get_objects():
		if isinstance(obj, City):
			print obj.name


def game(day = 0, max_days = DEFAULT_DAYS):
	lisbon = City("Lisbon")
	porto = City("Porto")
	jose = User("jose", lisbon)

	while(day <= max_days):
		print "DAY NUMBER %d" % day
		game_actions()
		action = raw_input(">")

		if action == "1":
			print "Cities you can move to:"
			get_all_cities()
		if action == "2":
			break

		day += 1


#Main game function
def main():
	

	game_welcome()
	a = raw_input(">")

	if a == "1":
		game()
	if a == "2":
		pass


if __name__ == '__main__':
	main()
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Define city classes


DEFAULT_DAYS = 3
CITY_LIST = []

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



def game(day = 1, max_days = DEFAULT_DAYS):
	lisbon = City("Lisbon")
	porto = City("Porto")

	CITY_LIST.append(lisbon)
	CITY_LIST.append(porto)

	jose = User("jose", lisbon)

	while(day <= max_days):
		print "DAY NUMBER %d" % day
		game_actions()
		action = raw_input(">")

		if action == "1":
			for city in CITY_LIST:
				print city.name

			print "\n Choose new city number:"
			new_city = raw_input(">")

			try:
				if int(new_city)
			except Exception, e:
				raise e
			if new_city.lower() in [x.name.lower() for x in CITY_LIST]:
				new



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
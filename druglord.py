#!/usr/bin/python
# -*- coding: utf-8 -*-

#Define city classes


DEFAULT_DAYS = 3
CITY_LIST = []
PLAYER_LIST = []

class City (object):
	def __init__ (self, name):
		self.name = name
		CITY_LIST.append(self)


#Define user classes
class User (object):
	def __init__(self, name, city):
		self.name = name
		self.city = city
		PLAYER_LIST.append(self)

	def get_city(self):
		return self.city.name

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

	jose = User("jose", lisbon)

	while(day <= max_days):

		for player in PLAYER_LIST:

			print "DAY NUMBER {} of {}".format(day, player.name)

			game_actions()
			action = raw_input(">")
			

			if action == "1":
				for (i, city) in enumerate(CITY_LIST):
					print city.name
				while True:
					print "\n Choose new city number or Q to go back:"
					new_city = raw_input(">")
					
					if new_city == "q":
						break

					try:
						try:
							new_city = CITY_LIST[int(new_city)]
							print "{} was in {}".format(jose.name, jose.get_city())
							jose.move_city(new_city)
							print "{} is now in {}".format(jose.name, jose.get_city())
							break
						except IndexError:
							print("{} is not a valid city.".format(int(new_city)))

					except ValueError:
						pass
						# try:
						# 	if new_city.lower() in [x.name.lower() for x in CITY_LIST]:
				



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
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Global values for the game, list of city, players and number of turns/days
DEFAULT_DAYS = 3
CITY_LIST = []
PLAYER_LIST = []

#Define city class
class City (object):
	# init city with its name and append the object to the list of cities (CITY_LIST)
	def __init__ (self, name):
		self.name = name
		CITY_LIST.append(self)


#Define user class
class User (object):
	# init city with its name and starting city and append the object to the list of players (PLAYER_LIST)
	def __init__(self, name, city):
		self.name = name
		self.city = city
		PLAYER_LIST.append(self)

		self.inventory = {"Cocaine":0, "Heroin":0}

	# Get the city where the player is
	def get_city(self):
		return self.city

	# move player to a new city object
	def move_city(self, new_city):
		self.city = new_city

# Write the "welcome screen"
def game_welcome():
	print "Welcome to Drug Lord"
	print "Choose an option:"
	print "1) New Game"
	print "2) Exit"

# Write possible turn actions
def game_actions():
	print "1) Move City"
	print "2) Exit"


# Game Cycle
def game(day = 1, max_days = DEFAULT_DAYS):

	# Create cities and player here because i haven't created a settings screen
	lisbon = City("Lisbon")
	porto = City("Porto")
	jose = User("Jose", lisbon)

	# Play the game while the number of days/turns is under the max
	while(day <= max_days):

		# Each player has its turn during the day
		for player in PLAYER_LIST:

			# Inform the player of its turn number
			print "DAY NUMBER {} of {}".format(day, player.name)

			#print possible actions
			game_actions()
			# wait for action that player wants to take
			action = raw_input(">")
			
			# response to move action
			if action == "1":
				#print available cities to trabel to
				for (i, city) in enumerate(CITY_LIST):
					print city.name

				#Wait for user input to be correct and perform an action
				while True:
					# Inform player of required action and wait for input
					print "\n Choose new city number or Q to go back:"
					new_city = raw_input(">")
					
					# Back to action menu
					if new_city == "q":
						break

					# or try to convert recieved input into a city player can move to
					try:
						try:
							#Try to get city of index new_city
							new_city = CITY_LIST[int(new_city)]
							# if possible, inform player of current city, move him and inform final city
							print "{} was in {}".format(jose.name, jose.get_city().name)
							jose.move_city(new_city)
							print "{} is now in {}".format(jose.name, jose.get_city().name)

							# exit move action and back to main menu
							break
						except IndexError:
							# Print if index doesn't have a city object
							print("{} is not a valid city.".format(int(new_city)))

					except ValueError:
						
						print "\n Estamos no ValueError \n"
						if new_city.lower() in [city.name.lower() for city in CITY_LIST]:
							new_city = [city.name.lower() for city in CITY_LIST].index(new_city.lower())

							print "{} was in {}".format(jose.name, jose.get_city().name)
							jose.move_city(CITY_LIST[new_city])
							print "{} is now in {}".format(jose.name, jose.get_city().name)
							break

						else:
							print("{} is not a valid city.".format(new_city))

				



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
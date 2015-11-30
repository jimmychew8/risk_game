"""Simulates the rolling of the die for a risk game."""

import sys 
from random import randint

def simulate(number_attacking, number_defending):
	"""Returns a tuple with the result of the attack."""

	while number_attacking > 1 and number_defending > 0: 

		# One attacking die, one defending die
		if number_attacking == 2 and number_defending == 1:

			attacker_roll = randint(1,6)
			defender_roll = randint(1,6)

			if attacker_roll > defender_roll:

				number_defending -= 1

			else:

				number_attacking -= 1

		# One attacking die, two defending die
		if number_attacking == 2 and number_defending > 1:

			attacker_roll = randint(1,6)
			defender_roll = [randint(1,6) for i in range(2)]

			if attacker_roll > defender_roll[0] and attacker_roll > defender_roll[1]:

				number_defending -= 1

			else:

				number_attacking -= 1

		# Two attacking die, one defending die
		if number_attacking == 3 and number_defending == 1:

			attacker_roll = [randint(1,6) for i in range(2)]
			defender_roll = randint(1,6)

			if attacker_roll[0] > defender_roll or attacker_roll[1] > defender_roll:

				number_defending -= 1

			else: 

				number_attacking -= 1

		# Two attacking die, two defending die
		if number_attacking == 3 and number_defending >= 2: 

			attacker_roll = sorted([randint(1,6) for i in range(2)], reverse=True)
			defender_roll = sorted([randint(1,6) for i in range(2)], reverse=True)

			for i in range(2):

				if attacker_roll[i] > defender_roll[i]:

					number_defending -= 1

				else:

					number_attacking -= 1

		# Three attacking die, one defending die
		if number_attacking > 3 and number_defending == 1:

			attacker_roll = [randint(1,6) for i in range(3)]
			defender_roll = randint(1,6)

			if attacker_roll[0] > defender_roll or attacker_roll[1] > defender_roll or attacker_roll[2] > defender_roll:

				number_defending -= 1

			else: 

				number_attacking -= 1

		# Three attacking die, two defending die
		if number_attacking > 3 and number_defending >= 2:

			attacker_roll = sorted([randint(1,6) for i in range(3)], reverse=True)
			defender_roll = sorted([randint(1,6) for i in range(2)], reverse=True)

			for i in range(2):

				if attacker_roll[i] > defender_roll[i]: 

					number_defending -= 1

				else:

					number_attacking -= 1

		if number_defending == 0:


			return number_attacking, number_defending

		if number_attacking == 1: 


			return number_attacking, number_defending


if __name__ == '__main__':

	if len(sys.argv) != 3:

		print "Enter: number of attacking players, number of defending players."

	else:

		simulate(sys.arvg[1], sys.argv[2])

			

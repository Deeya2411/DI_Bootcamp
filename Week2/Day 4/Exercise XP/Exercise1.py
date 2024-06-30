import random

def get_random_temp(season):
	
	if (season == 'Winter'):
		randomTemp = random.randint(-10, 16)

	elif (season == 'Autumn'):
		randomTemp = random.randint(17, 23)

	elif (season == 'Summer'):
		randomTemp = random.randint(32, 40)	

	else:
		randomTemp = random.randint(24, 32)
	
	#Part 1
	#numRandom = random.randint(-10, 40)
	#result = get_random_temp()
	#print (result)

	return randomTemp

def main(season):
	randomTemp = get_random_temp(season)

	print("The temperature right now is " + str(randomTemp) + " degrees Celsius.")

	if (randomTemp < 0):
		print("Brrr, that’s freezing! Wear some extra layers today")
	
	elif ( 0 <= randomTemp < 16):
		print ("Quite chilly! Don’t forget your coat")

	elif ( 16 <= randomTemp < 23):
		print ("Average! Take a coat in case of need")

	elif ( 24 <= randomTemp < 32):
		print ("Awesome! Perfect weather for a picnic")

	else:
		print ("Too hot! It seems like in a sauna")



season = input("Enter a season(Summer, Autumn, Winter, Spring): ")

main(season)
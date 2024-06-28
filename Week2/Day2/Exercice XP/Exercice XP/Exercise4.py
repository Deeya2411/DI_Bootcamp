import random

numInput = input("Enter a number between 1 and 100: ")

numRandom = random.randint(1, 100)

def compare(numInput, numRandom):
	if numInput == numRandom: 
		print("Yuppy, it's a match")
	else:
		print(f"Try again!! {numInput}  &  {numRandom}")

x = compare(numInput,numRandom)

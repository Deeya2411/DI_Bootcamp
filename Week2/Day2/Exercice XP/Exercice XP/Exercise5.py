size = input("Enter the size T-Shirt: ")

text = input("Enter the text of message to be printed: ")


def make_shirt(size, text):
	
	size = "Large"
	
	text = "I love Python"

	if (size == "Large" or size == "L"):
		
		text = "I love Python"

	elif (size == "Medium" or size == "M"):
		
		text = "I love Python" 	

	print(f"The size of the shirt is {size} and the text is {text}")

output = make_shirt(size, text)




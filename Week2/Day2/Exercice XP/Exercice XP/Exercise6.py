magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'] 

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magician_names)

def make_great(magicians):
	for magician in magicians:
		return ("The Great " +  magician.title())

print (make_great(magician_names))




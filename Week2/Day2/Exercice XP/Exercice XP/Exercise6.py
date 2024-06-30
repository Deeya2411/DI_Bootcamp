def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = 'The Great ' + magician 
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)

print("\n")
make_great(magician_names)
show_magicians(magician_names)

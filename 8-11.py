def show_magicians(names):
	""" 
	function to take names from a list and pass to the function  
	"""
	#create for loop to store and print each magician nam
	for name in names:
		print(name.title())

def make_great(names):
	""" 
	function to take names from a list and modifies the list to add "the great" at the end of each name
	"""
	#build a new list to hold the modified names from the original list
	great_magicians = []
	#create a while loop to append "the Great" to the end of each name 
	while names:
		name = names.pop()
		great_magician = name + ' the great'
		great_magicians.append(great_magician)
	#add great magicians back into names liste
	for great_magician in great_magicians:
		names.append(great_magician)
	return names

#create list of magicians and call back the function to print the list of names
names = ['mysterio', 'david blaine', 'houdini']
show_magicians(names)

#call show_magicians with a copy of the names list so the orignal is unchanged
print("\nGreat magicians:")
great_magicians = make_great(names[:])
show_magicians(great_magicians)

#call show magicians with original list
print("\nOriginal magicians:")
show_magicians(names)


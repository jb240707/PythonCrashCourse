def show_magicians(names):
	""" 
	for loop takes list of magician names and passes to the function  
	"""
	for name in names:
		print(name.title())

#create list of magicians and call back the function to print the list of names
m_names = ['mysterio', 'david blaine', 'houdini']
show_magicians(m_names)
#make an empty dictionary to fill with dream vacation spots 
dream_destinations = {}

#set a flag to indicate user polling is active
polling_active = True

#create a while loop to prompt users for their dream spot 
while polling_active:
	#prompt for user's name and chosen destination
	names = input("What is your name?")
	destinations = input("What is your dream vacation destination?")
	#store the user response in the dictionary
	dream_destinations[names] = destinations
	#find out if other users are going to respond
	repeat = input("Would anyone else like to participate? (yes/no)")
	if repeat == 'no':
		polling_active = False
	else:
		continue
	#print the results of the poll	
	print("****Poll Results****")
	for names, destinations in dream_destinations.items():
		print(names.title() + " would travel to " + destinations.title() + " for a dream vacation!")
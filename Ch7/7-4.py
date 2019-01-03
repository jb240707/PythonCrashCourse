#Write prompt for user to enter pizza toppings
prompt = "\nPlease enter your toppings:"
prompt+="\n(Enter 'quit' when finished.)"

#Loop through topping names and print 
#Print inputs until the user inputs quit
while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else: 
		print("Got it. We'll add " + toppings.title() + "!")
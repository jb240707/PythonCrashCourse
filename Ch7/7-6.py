#7-6a
#Write prompt for user to enter pizza toppings
prompt = "\nPlease enter your toppings:"
prompt+="\n(Enter 'quit' when finished.)"

#Use a break statement to exit the while loop after user enters 'quit'
#Print topping inputs 
while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else: 
		print("Got it. We'll add " + toppings.title() + "!")

#7-6b 
#Write prompt for user to enter age integer
prompt = "\nPlease enter your age to get ticket price: "

#Loop through age ranges for movie ticket prices with an active variable
#Print user's ticket price based on age integer
active = True
while active:
    age = int(input(prompt))
    if age == 0:
        continue
    elif age <= 2:
        print(str(age) + ". Your admission is free.")
    elif age <= 12:
        print(str(age) + ". Your admission is $10.")
    else:
        print(str(age) + ". Your admission is $15.")


#7-6c
#Write prompt for user to enter pizza toppings
prompt = "\nPlease enter your toppings:"
prompt+="\n(Enter 'quit' when finished.)"

#Use a conditional test to exit the loop after looping through topping names 
#Print inputs to let user know you'll add it, until the user inputs 'quit'
active = True
while active:
	toppings = input(prompt)
	if toppings == 'quit':
		active = False
	else: 
		print("Got it. We'll add " + toppings.title() + "!")
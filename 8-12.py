def sammich_maker(*toppings):
	""" Print the list of toppings that have been requested. """
	print("\nMaking a sammich with the following toppings:")
	for topping in toppings:
		print("-" + topping)
	print("Your sammich is made!")

sammich_maker('turkey', 'ham', 'cheddar', 'spinach', 'wheat')
sammich_maker('pepperoni', 'salami', 'italian sausage', 'provolone', 'hoagie')
sammich_maker('chicken', 'avocado', 'swiss', 'spinach', 'pita')
#Create a list of favorite pizzas to be used in a for loop. 
pizzas = ['meat lovers' , 'the supreme' , 'the great white']

#Create for loop to print the names of the pizzas. 
for pizza in pizzas:
	print(pizza.title() + " is an awesome pizza pie!\n")

#Print unique statement about each pizza, then a finishing statement at the end.
print(pizzas[0].title() + " is the best for carnivores.\n")
print(pizzas[1].title() + " at Boston's is my favorite currently.\n")
print(pizzas[2].title() + " at BJ's Brewhouse is an amazing Chicago style pizza.\n")
print("I really love a good pizza pie!!!")
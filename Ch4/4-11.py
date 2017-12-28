#Create a list of favorite pizzas to be used in a for loop. 
pizzas = ['meat lovers' , 'the supreme' , 'the great white']


#Start with program from 4-1 and make a copy of the list.  
#Add a new pizza to the original list. 
#Add a different pizza to the list friend_pizzas.
#Use a for loop to print the first list then again to print the second list to prove the lists are different.

friend_pizzas = pizzas[:]
pizzas.append('pepperoni')
friend_pizzas.append('alfredo')

print("\nMy favorite pizzas are:")
for toppings in pizzas:
	print(toppings)

print("\nMy friend's favorite pizzas are:")
for toppings in friend_pizzas:
	print(toppings)

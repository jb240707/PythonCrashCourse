#Create a list of animals with common characteristics and store in a list. 
common_animals = ['kittens' , 'puppies' , 'bunnies']

#Create a for loop to print a statement about each animal. 
for animal in common_animals:
	print(animal.title() + " make lovable pets and have personailties of their own.\n")

#Print the message a use a slice to print the first three items from the list. 
print(common_animals[0:3])

#Print the message and use a slice to print three items from the middle of the list.
print("\nThree items from the middle list are:")
print(common_animals[:])

#Print the message and use a slice to print the last three items in the list. 
print("\nThree last three items in the list are:")
print(common_animals[-3:])
#Ask the user for a number
number = input("Please enter a number, any number. ")
#Convert the user input to an integer
number = int(number)

#Report whether the number is a multiple of 10 or not using an if-else chain
if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10!")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")
#Create a variable call alien_color and assign a value or yellow green or red.
alien_color = 'green'

#Write if statement to test if alien's color is green.
#If so, print message that says player has earned five points. 
#Wite elif statement in to award 10 points. 
#Fist run should run the if block.
if alien_color == 'green':
	award = 5
	print("You shot down a green alien. You earned " + str(award) + " bonus points!")
elif alien_color != 'green':
	award = 10
	print("You did not shoot down a green alien. You earned " + str(award) + " bonus points!")


#Write a version of the same program that runs the if block.
alien_color = 'yellow'

#Write if statement to test if alien's color is green.
#If so, print message that says player has earned five points. 
if alien_color == 'green':
	award = 5
	print("You shot down a green alien. You earned " + str(award) + " bonus points!")
elif alien_color != 'green':
	award = 10
	print("You did not shoot down a green alien. You earned " + str(award) + " bonus points!")




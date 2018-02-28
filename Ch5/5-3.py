#Create a variable call alien_color and assign a value or yellow green or red.
alien_color = 'green'

#Write if statement to test if alien's color is green.
#If so, print message that says player has earned five points. 
if alien_color == 'green':
    award = 5
    print("You shot down a green alien. You earned " + str(award) + " bonus points!")
else:
    award = 0
    print("You did not shoot down a green alien. You earned " + str(award) + " bonus points.")


#Write a version of the same program that fails.
alien_color = 'yellow'

#Write if statement to test if alien's color is green.
#If so, print message that says player has earned five points. 
if alien_color == 'green':
    award = 5
    print("You shot down a green alien. You earned " + str(award) + " bonus points!")
else:
    award = 0
    print("You did not shoot down a green alien. You earned " + str(award) + " bonus points.")




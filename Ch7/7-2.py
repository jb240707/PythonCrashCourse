#Ask the customer how many people are in their dinner party
party = input("How many people are in your dinner party? ")

#Prompt for an answer as an integer to get the number of people
party = int(party)

#Write if-elif chain to find out if the party is more than 8
if party > 8:
    print("\nThere will be a bit of a wait while we get your table ready.")
else:
    print("\nYour table is right this way!")
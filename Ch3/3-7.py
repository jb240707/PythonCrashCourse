guests = ['ken griffey jr.' , 'troy aikman' , 'john constantine']

#Same as 3-4 only state that Aikman cannot make it to dinner. 
print("The Kid! Please come chow down, " + guests[0].title())
print("Please bring your rings to dinner, " + guests[1].title() + ".")
print("It's " + guests[2].title() + "... Asshole. Please come to dinner.")
print(guests[1].title() + " can't make it to dinner. ")

#Now replace Aikman with brady in the guest list, then print new messages to guests. 
guests[1] = 'tom brady'

print("\nThe Kid! Please come chow down, " + guests[0].title())
print(guests[1].title() + ", the GOAT, please bring your rings to dinner.")
print("It's " + guests[2].title() + "... Asshole. Please come to dinner.\n")

#Now insert more guests within the list and append one more guest to the end of the list, then print new messages to the guests and let them know we have a bigger table. 
guests.insert(0, 'mickey mantle')
guests.insert(1, 'john wick')
guests.append('raylan givens')

print(guests[0].title() + ", bring your ass back from the dead and eat.")
print(guests[1].title() + ", give me one of those gold coins for some dinner.")
print("The Kid! Please come chow down, " + guests[2].title())
print(guests[3].title() + ", the GOAT, please bring your rings to dinner.")
print("It's " + guests[4].title() + "... Asshole. Please come to dinner.")
print(guests[5].title() + ", come on back to Harlan for dinner.")
print("All, I've found a bigger dinner table!")

#Just found out we can only invite two guests because the larger dinner table will not arrive on time. 
print("\nAll, bad news, I can only invite two people now.\n")

#Pop names one at a time and then write a message to the guests being popped from the list to apologize and remember the list shrinks each time a name is popped.
popped_one = guests.pop(0)
popped_two = guests.pop(1)
popped_three = guests.pop(3)
popped_four = guests.pop(2)

print(popped_one.title() + ", sorry but not sorry. You're uninvited.")
print("Keep it real, but you're uninvited, " + popped_two.title())
print(popped_three.title() + ", stay down in Miami. Dinner is off.")
print(popped_four.title() + ", you can stay home and smoke.\n")


#Use del to remove last two names on the list and then print the list to ensure the list is empty. 
del guests[0]
del guests[0]
print(guests)

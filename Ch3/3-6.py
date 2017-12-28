guests = ['ken griffey jr.' , 'troy aikman' , 'john constantine']


print("The Kid! Please come chow down, " + guests[0].title())
print("Please bring your rings to dinner, " + guests[1].title() + ".")
print("It's " + guests[2].title() + "... Asshole. Please come to dinner.")
print(guests[1].title() + " can't make it to dinner. ")


guests[1] = 'tom brady'

print("\nThe Kid! Please come chow down, " + guests[0].title())
print(guests[1].title() + ", the GOAT, please bring your rings to dinner.")
print("It's " + guests[2].title() + "... Asshole. Please come to dinner.\n")

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










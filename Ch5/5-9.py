#Write an empty list to store usernames.
usernames = []


#Write an if else chain to find out if the list is empty.
#If not empty print a statement to welcome the user using a for loop.
#If empty print a statement. 
if usernames:   
    for username in usernames:
        print(username.title() + ", welcome to thunder dome, bitch!")
else:       
     print("We need some damn users!")
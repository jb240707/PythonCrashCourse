#Write a list of five or more existing usernames.
existing_usernames = ['admin', 'bill', 'jack', 'meoff', 'dick']

#Write a list containing a few new usernames and a couple of the existing.
new_usernames = ['beavis', 'rico', 'Jack', 'meoff', 'Maurice']

#Write a for loop to find out if new user names requested are in the existing 
#usernamelist by looping through the new names.
for new_username in new_usernames:   
    if new_username in existing_usernames:
        print("Seat's taken... " + new_username.lower() + " is in use! Choose a new one.")
    else:       
        print(new_username.lower() + " is yours! Welcome.")
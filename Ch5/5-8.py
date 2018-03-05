#Write a list of five or more usernames.
usernames = ['admin', 'bill', 'jack', 'meoff', 'dick']


#Write a for loop with if-else chain to make a custom greeting for the admin and 
#a generic greeting for the rest.
for username in usernames:  
    if username == 'admin':
        print("Hello again " + username.title() + ", the Obergrupenfeuher. Welcome.")
    elif username != 'admin':
        print(username.title() + ", welcome to thunder dome, bitch!")
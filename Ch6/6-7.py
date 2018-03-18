#Create three dictionaries describing three friends
friend_steph = {
    'fitst_name': 'steph', 'last_name': 'bryant', 'age': '25', 'city': 'northlake',
    }

friend_john = {
    'fitst_name': 'john', 'last_name': 'king', 'age': '34', 'city': 'coppell',
    }

friend_justin = {
    'fitst_name': 'justin', 'last_name': 'bryant', 'age': '31', 'city': 'japland',
    }

#Create a list to store each dictionary
people = [friend_steph, friend_john, friend_justin,]

#Create a for loop to loop  through all info and print all info
for friend in people:
    print(friend)

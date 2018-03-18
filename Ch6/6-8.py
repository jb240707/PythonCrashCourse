#Create multiple dictionaries describing pets
pet_1 = {
    'name': 'raider', 'type': 'dog', 'breed': 'lab', 'fur': 'short black',
    }

pet_2 = {
    'name': 'riot', 'type': 'dog', 'breed': 'lab', 'fur': 'short yellow',
    }

pet_3 = {
    'name': 'rocket', 'type': 'dog', 'breed': 'mutt', 'fur': 'short black',
    }

pet_4 = {
    'name': 'TC', 'type': 'cat', 'breed': 'unknown', 'fur': 'black and white',
    }

#Create a list to store each dictionary
pets = [pet_4, pet_3, pet_2, pet_1,]

#Create a for loop to loop  through all info and print all info
for pet in pets:
    print(pet)

#Create dictionary with names as keys and each person's favorite places
favorite_places = {
    'jason': ['florida', 'south padre', 'fort worth',], 'steph': ['galveston', 'fort worth', 'denton',], 'dave': ['lampasas', 'vegas', 'austin',],
    }

#Create a for loop to loop the names printing favorite places for each
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
    
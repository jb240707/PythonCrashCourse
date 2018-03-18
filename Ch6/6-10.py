#Create a dictionary so each person's name can have one more favorite number
fav_numbers = {
        'jason': ['7', '24',], 'troy': ['8', '11',], 'tom': ['12', '11',], 'justin': ['4', '12',], 'drew': ['9', '11',],
        }

#Create a for loop to loop the names printing favorite numberss for each
for name, numbers in fav_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number.title())
    
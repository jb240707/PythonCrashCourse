#Create a tuple to store a list of five basic foods.
buffet_foods = ('chicken wings', 'roast beef', 'baked potatoes', 'sirloin', 'hot rolls')

#Create a for loop to print each food offered.
for basic in buffet_foods:
    print(basic)

#Try to replace an item in the tuple and make sure python rejects the change.
buffet_foods[1] = ('carved turkey')

#Create a revised menu tuple to store a list of new basic foods.
buffet_foods = ('chicken wings', 'ham', 'baked potatoes', 'sirloin', 'corn bread')

#Create a for loop to print each food offered.
for basic in buffet_foods:
    print(basic)
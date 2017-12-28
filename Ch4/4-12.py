#foods.py from Ch 4 section.
my_foods = ['pizza' , 'falafel' , 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

#Take previous version and write two for loops to print each separate list of foods.
print("My favorite foods are:")
for items in my_foods:
    print(items)

print("\nMy friend's favorite foods are:")
for items in friend_foods:
    print(items)
#Write prompt for user to enter age integer
prompt = "\nPlease enter your age to get ticket price: "

#Loop through age ranges for movie ticket prices
#Print user's ticket price based on age integer
active = True
while active:
    age = int(input(prompt))
    if age <= 2:
        print(str(age) + ". Your admission is free.")
    elif age <= 12:
        print(str(age) + ". Your admission is $10.")
    else:
        print(str(age) + ". Your admission is $15.")
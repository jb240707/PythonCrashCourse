#Write a while loop that never ends and requires ctrl+C to exit
active = True
#Set age to provide a finite value for the while loop
age = 1
while active:
    if age == 0:
        continue
    elif age <= 2:
        print(str(age) + ". Your admission is free.")
    elif age <= 12:
        print(str(age) + ". Your admission is $10.")
    else:
        print(str(age) + ". Your admission is $15.")

#Write a list containing the numbers 1 through 9.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Write a for loop to find the ordinal ending for each listed number. 
#Use an if-elif chain inside a for loop to print each number and ending.
for number in numbers:   
    if number == '1':
        print(number + "st\n")
    elif number == '2':
        print(number + "nd\n")
    elif number == '3':
        print(number + "rd\n")
    else:       
        print(number + "th\n")
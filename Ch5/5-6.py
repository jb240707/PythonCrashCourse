#Write if-elif-else chain to determine stages of life. Value for variable age.
age = 89

#Write if-elif-else chain for various age ranges and print comments.
if age < 2:
    print("The person is a baby!")
elif age >= 2 and age < 4:
    print("The person is a toddler!")
elif age >= 4 and age < 13:
    print("The person is a kid!")
elif age >= 13 and age < 20:
    print("The person is a teen!")
elif age >= 20 and age < 65:
    print("The person is an adult!")
else:
    print("The person is an elder!")
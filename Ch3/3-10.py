#Make a new list of scotches you love.
scotches = ['glennmorangie signet' , 'macallan 12' , 'tahmdhu 10']
print(scotches)


#Make a statement about your favorite scotch and print it with title().  
print("\nI think " + scotches[0].title() + " is the most unique and declious of all.")



#Replace one scotch on the list with another you love and make a new statement as to why then print it.
scotches[2] = 'glennmorangie 18'

print("\nReplacing Tamdhu with an older and wiser " + scotches[2].title() + ".\n")



#Now insert another 18 year, remove any 12 year, and add another favorite 19 year to the end.
scotches.insert(1, 'balvenie 18')
scotches.remove('macallan 12')
scotches.append('aberlour 18')



#Print the name of the new scotch in the 3rd position and tell where it ranks in your opinion.
print(scotches[3].title() + " is a dark horse as one of the best. Both affordable and amazing.\n")



#Print a message indicating how many scotches are listed, or the length of the list. 
print(len(scotches))



#Pop the necessary names and print a message about the changes to the list. 
popped = scotches.pop(0)
print("\nI love it but this list is only for 18 year old scotches, " + popped.title() + ".\n")



#Use del to remove the scotch less preferred and print the last standing.
del scotches[1]
print(scotches)



#Print list sorted in alphabetical order. 
print(sorted(scotches))



#Print list in original order again. 
print(scotches)


#Print in reverse order. 
scotches.reverse()
print(scotches)



#Reverse order again. 
scotches.reverse()
print(scotches)



#Sort list permanently in alphabetical order.
scotches.sort() 
print(scotches)



#Re-sort list permanently in reverse alphabetical order.
scotches.sort(reverse=True) 
print(scotches)


#Print best item for last on the list. 
print(scotches[-1])
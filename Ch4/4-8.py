#Create a list of cubes for integers 1 through 10.
#Use a for loop to print the value of each cube. 
cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)

print(cubes)
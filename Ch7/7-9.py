#Make a list of sandwiches and fill it with sandwich names 
sandwich_orders = ['hoagie', 'pastrami', 'turkey', 'pastrami', 'ham', 'italian', 'pastrami', 'philly']

#Make an empty list for completed sandwich orders
finished_sandwiches = []

#create a while loop to remove orders for pastrami from the list above
#Print a message indicating the deli is out of pastrami
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	print("The deli is currently out of pastrami.")

#Loop through list of sandwich orders and print a message for each
#As sandwiches are made, move each to the finished list
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("Finishing order: " + current_order.title())
    finished_sandwiches.append(current_order)

 #After all are made print a message listing all sandwich orders completed
print("\nThe following orders have been completed:")
for finished_order in finished_sandwiches:
	print(finished_order.title())
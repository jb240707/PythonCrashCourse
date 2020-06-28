class Restaurant():
    """ 
    class to define attributes for restaurant instances and indicate if they're open or not
    """
    def __init__(self, restaurant_name, cuisine_type):
        """ 
        initialize restaurant name and cuisine type 
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        simulate output of restaurant description inputs 
        """
        print(self.restaurant_name.title() + " serves delicious " + self.cuisine_type + "!")

    def open_restaurant(self):
        """ 
        simulate output indicating whether or not restaurant is open
        """
        print(self.restaurant_name.title() + " is open for business!")

    def set_number_served(self):
        """ 
        simulate output indicating number of customers served
        """
        print(self.restaurant_name.title() + " has served " + str(self.number_served) + " plus customers!")

    def increment_number_served(self, customers):
        """ 
        simulate output indicating incremented number of customers served
        """
        self.number_served += customers

#create an instance of the class above to describe the restaurant
my_restaurant = Restaurant('little italy', 'pizza')
restaurant = Restaurant('moo cow', 'beef ribs')
my_restaurant.describe_restaurant()
restaurant.describe_restaurant()
my_restaurant.open_restaurant()
restaurant.open_restaurant()

#create an instance of the class above to describe number of customers served
print(restaurant.set_number_served())
restaurant.number_served = 999
restaurant.set_number_served()

#create an instance of the class above to increment customers served
restaurant.increment_number_served(2000)
restaurant.set_number_served()
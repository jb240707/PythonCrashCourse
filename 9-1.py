class Restaurant():
    """ 
    class to define attributes for restaurant instances and indicate if they're open or not
    """
    def __init__(self, restaurant_name, cuisine_type):
        """ initialize restaurant name and cuisine type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ simulate output of restaurant description inputs """
        print(self.restaurant_name.title() + " serves delicious " + self.cuisine_type + "!")

    def open_restaurant(self):
        """ 
        simulate output indicating whether or not restaurant is open
        """
        print(self.restaurant_name.title() + " is open for business!")

my_restaurant = Restaurant('little italy', 'pizza')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
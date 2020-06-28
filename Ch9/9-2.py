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
        """ simulate output indicating whether or not restaurant is open """
        print(self.restaurant_name.title() + " is open for business!")

my_restaurant = Restaurant('little italy', 'pizza')
other_restaurant = Restaurant('meat u anywhere', 'brisket')
spare_restaurant = Restaurant('matitos', 'margaritas')

my_restaurant.describe_restaurant()
other_restaurant.describe_restaurant()
spare_restaurant.describe_restaurant()
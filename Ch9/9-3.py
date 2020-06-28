class User():
    """  class to define attributes for user profiles """
    
    def __init__(self, first_name, last_name, email_address, contact_phone, home_city, job_role):
        """ initialize user attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_phone = contact_phone
        self.home_city = home_city
        self.job_role = job_role

    def describe_user(self):
        """ simulate output of user summary inputs """
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.job_role.title() + " from " + self.home_city.title() + ".")

    def greet_user(self):
        """ simulate output of a personal greeting based on attributes """
        print("Welcome to the event,  " + self.first_name.title() + "! Are " + self.email_address + " and " + self.contact_phone + " still the best way to contact you about future events?")

my_profile = User('jason', 'bryant', 'a@nope.com', '111-111-1111', 'dallas', 'ninja')
his_profile = User('dad', 'bryant', 'b@nope.com', '222-222-2222', 'dallas', 'nerd')
her_profile = User('addy', 'bryant', 'c@nope.com', '333-333-3333', 'northlake', 'teether') 

my_profile.describe_user()
his_profile.describe_user()
her_profile.describe_user()
my_profile.greet_user()
his_profile.greet_user()
her_profile.greet_user()
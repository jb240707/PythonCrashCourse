class User():
    """ class to define attributes for user profiles """
    
    def __init__(self, first_name, last_name, email_address, contact_phone, home_city, job_role):
        """ initialize user attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_phone = contact_phone
        self.home_city = home_city
        self.job_role = job_role
        self.login_attempts = 0

    def describe_user(self):
        """ simulate output of user summary inputs """
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.job_role.title() + " from " + self.home_city.title() + ".")

    def greet_user(self):
        """ simulate output of a personal greeting based on attributes """
        print("Welcome to the event,  " + self.first_name.title() + "! Are " + self.email_address + " and " + self.contact_phone + " still the best way to contact you about future events?")

    def increment_login_attempts(self, logins=1):
        """ simulate output of incrementing logins by 1 on each attempt """
        self.login_attempts += logins
        print(self.login_attempts)

    def reset_login_attempts(self, logins=0):
        """ if output of logins is > 0 then reset it when called """
        if logins <= self.login_attempts:
            self.login_attempts = logins
            print(self.login_attempts)
        else:
            print("This user still has no logins!") 

#instances to show and increment number of user logins
my_profile = User('jason', 'bryant', 'a@nope.com', '111-111-1111', 'dallas', 'ninja')
my_profile.describe_user()
my_profile.increment_login_attempts()
my_profile.increment_login_attempts()
my_profile.increment_login_attempts()
my_profile.reset_login_attempts()

#instances to show and increment number of user logins
his_profile = User('dad', 'bryant', 'b@nope.com', '222-222-2222', 'dallas', 'nerd')
his_profile.describe_user()
his_profile.increment_login_attempts()
his_profile.increment_login_attempts()
his_profile.increment_login_attempts()
his_profile.reset_login_attempts()

#instances to show and increment number of user logins
her_profile = User('addy', 'bryant', 'c@nope.com', '333-333-3333', 'northlake', 'teether') 
her_profile.describe_user()
her_profile.increment_login_attempts()
her_profile.increment_login_attempts()
her_profile.increment_login_attempts()
her_profile.reset_login_attempts()
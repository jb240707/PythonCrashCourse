#!make_car.py

def make_car(make,model,**car_info):
    """ build a dictionary containing everything we know about a desired car """
    #create dictionary to which we'll pass the keys and values
    profile = {
        'make': make.title(),
        'model': model.title(),
    }
    #write a for loop to loop through and collect the make and model
    for key, value in car_info.items():
        profile[key] = value
    #return the foundation profile information
    return profile

#call the make_car fuction and ensure it will accept arbitrary arguements
car_profile = make_car('gmc','sierra 1500',color='silver',towing_package=True)
print(car_profile)
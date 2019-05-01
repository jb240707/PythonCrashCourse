#attempt to call function in car_profile.py with various methods
import car_profile

#call the make_car fuction and ensure it will accept arbitrary arguements
car_profile.make_car('gmc','sierra 1500',color='silver',towing_package=True)

#attempt to call function in car_profile.py with various methods
from car_profile import make_car

#call the make_car fuction and ensure it will accept arbitrary arguements
car_profile.make_car('gmc','sierra 1500',color='silver',towing_package=True)

#attempt to call function in car_profile.py with various methods
from car_profile import make_car as mc 

#call the make_car fuction and ensure it will accept arbitrary arguements
mc('gmc','sierra 1500',color='silver',towing_package=True)

#attempt to call function in car_profile.py with various methods
import car_profile as cp 

#call the make_car fuction and ensure it will accept arbitrary arguements
cp.make_car('gmc','sierra 1500',color='silver',towing_package=True)

#attempt to call function in car_profile.py with various methods
from car_profile import *

#call the make_car fuction and ensure it will accept arbitrary arguements
car_profile.make_car('gmc','sierra 1500',color='silver',towing_package=True)

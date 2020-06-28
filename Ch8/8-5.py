def describe_city(city_name, country='united kingdom'):
	""" function which provides a city name and to which country it belongs """
	print(city_name.title() + " is in " + country.title() + ".")

describe_city(city_name='glasgow')
describe_city('watford')
describe_city('cork', country='Ireland')
#Function takes in name of city and its country then return a string 
def city_country(city_name, country):
	""" function returns city name, country name neatly formatted """
	full_city_country = city_name + ', ' + country
	return full_city_country.title()

formatted = city_country('santiago', 'chile')
print(formatted)
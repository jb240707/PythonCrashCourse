#Create a dictionary with three cities and three keys for each one
cities = {
    'amsterdam': { 
        'country': 'netherlands',
        'population': '1 milly',
        'fact': 'Lots of weed man!',
        },
    'Boca': {
        'country': 'united states',
        'population': 'dunno',
        'fact': 'Won a baseball tournament!',
        },
    'london': {
        'country': 'united kingdom',
        'population': '1 billy',
        'fact': 'Fucking Sherlock Holmes!',
        },
    }
    
#Print city name and listed information about city below it
for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info['country']
    fact = city_info['fact']
    population = city_info['population']
    print("\tCountry: " + country.title())
    print("\tFact: " + fact)
    print("\tPopulation: " + population.title())
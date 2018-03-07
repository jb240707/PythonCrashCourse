major_rivers = {
    'nile': 'egypt',
    'mississippi': 'the united states',
    'amazon': 'peru',
    }

for name, country in major_rivers.items():
    print("The " + name.title() + " river flows through " + country.title() + ".")

for name in major_rivers.keys():
    print(name.title())

for country in major_rivers.values():
    print(country.title())
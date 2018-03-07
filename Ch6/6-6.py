favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

voters = ['phil', 'sarah', 'john',]

for names in favorite_languages.keys():
    print(names.title())
    
    if names in voters:
        print(names.title() + ", thanks for voting dude!!")
    elif names not in voters:
        print(names.title() + ", come get your damn vote on!!")
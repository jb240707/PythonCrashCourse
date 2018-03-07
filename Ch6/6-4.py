glossary = {
    'a dictionary': 'is a collection of key value pairs to connect information',
    'a list': 'is a muteable, changeable, ordered sequence of elements',
    'a loop': 'iterates through members of a sequence in order',
    'a key': 'is made up of a value or element in a dictionary', 
    'a value': 'is information describing a key or object',
    }

for word, meaning in glossary.items():
    print(word.title() + " " + meaning + ".")  
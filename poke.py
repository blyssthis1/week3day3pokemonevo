""" aExercise 1:
Create a Method prints an image of your pokemon"""

from IPython.display import Image
display(Image('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/245.png', width = 200))

class Pokemon:
    def __init__(self,name):
        self.name = name
        self.types = None
        self.weight = None
        self.abilities = None
        self.sprite = None
        self.poke_api_call()
    def poke_api_call(self):
        # Use the pokemon parameter to make a request to the pokeapi
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}/')
        # if the status code is 200:
        if response.status_code == 200:
            # Get the pokemon's data with the json method
            data = response.json()
            # Pull out the name, weight, types, abilities
            self.name = data['name']
            types = data['types']
            self.types = list(map(lambda x: x['type']['name'], types))
            self.weight = data['weight']
            abilities = data['abilities']
            self.abilities = list(map(lambda x: x['ability']['name'], abilities))
            self.sprite = data['sprites']['front_default']
            # if the status code is not 200, print an error message
        else:
            print(f'ERROR, STATUS CODE {response.status_code}')
    def display_pokemon(self):
        display(Image(self.sprite, width = 300))

pikachu = Pokemon('pikachu')    
pikachu.display_pokemon()

"""Exercise 2:
Create a Method that evolves your Pokemon"""

pikachu = Pokemon('pikachu')

print(pikachu.sprite)
pikachu.evolve()
pikachu.sprite
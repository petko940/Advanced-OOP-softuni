from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {Pokemon.pokemon_details(pokemon)}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemons_name):
        for x in self.pokemons:
            if pokemons_name == x.name:
                self.pokemons.remove(x)
                return f"You have released {pokemons_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for x in self.pokemons:
            output += f"- {x.pokemon_details()}\n"
        return output


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, ):
        self.name = name
        self.pokemons: list = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return f"Pokemon is not caught"
        for name in self.pokemons:
            if name.name == pokemon_name:
                self.pokemons.remove(name)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        output = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        [output.append(f"- {x.pokemon_details()}") for x in self.pokemons]
        return '\n'.join(output)


from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self, ):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    @property
    def aquarium_types(self):
        return {"FreshwaterAquarium": FreshwaterAquarium,
                "SaltwaterAquarium": SaltwaterAquarium}

    @property
    def decoration_types(self):
        return {"Ornament": Ornament,
                "Plant": Plant}

    @property
    def fish_types(self):
        return {"FreshwaterFish": FreshwaterFish,
                "SaltwaterFish": SaltwaterFish}

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aquarium_types.keys():
            return "Invalid aquarium type."
        new_aquarium = self.aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.decoration_types:
            return "Invalid decoration type."

        new_decoration = self.decoration_types[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.find_object(aquarium_name, "name", self.aquariums)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)

            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.find_object(aquarium_name, "name", self.aquariums)
        if aquarium:
            if (aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "SaltwaterFish") \
                    or (aquarium.__class__.__name__ == 'SaltwaterAquarium' and fish_type == "FreshwaterFish"):
                return "Water not suitable."

            new_fish = self.fish_types[fish_type](fish_name, fish_species, price)
            massage = aquarium.add_fish(new_fish)
            return massage

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_object(aquarium_name, "name", self.aquariums)
        if aquarium:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_object(aquarium_name, "name", self.aquariums)
        if aquarium:
            fish_price = sum(fish.price for fish in aquarium.fish)
            decorations_price = sum(d.price for d in aquarium.decorations)
            value = fish_price + decorations_price
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        [result.append(str(x)) for x in self.aquariums]
        return "\n".join(result)


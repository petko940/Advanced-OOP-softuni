from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission_count = 0
        self.not_successful_mission_count = 0

    @property
    def valid_astronaut_types(self):
        return {"Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.valid_astronaut_types:
            raise Exception("Astronaut type is not valid!")

        try:
            next(x for x in self.astronaut_repository.astronauts if x.name == name)
        except StopIteration:
            new_astronaut = self.valid_astronaut_types[astronaut_type](name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

        return f"{name} is already added."

    def add_planet(self, name: str, items: str):
        try:
            next(x for x in self.planet_repository.planets if x.name == name)
        except StopIteration:
            new_planet = Planet(name)
            new_planet.items.extend(items.split(', '))
            self.planet_repository.add(new_planet)
            return f"Successfully added Planet: {name}."

        return f"{name} is already added."

    def retire_astronaut(self, name: str):
        try:
            astronaut = next(x for x in self.astronaut_repository.astronauts if x.name == name)
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"
        except StopIteration:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        try:
            planet = next(x for x in self.planet_repository.planets if x.name == planet_name)
        except StopIteration:
            raise Exception("Invalid planet name!")

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        suitable_astronauts = [x for x in sorted_astronauts[:5] if x.oxygen > 30]

        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        count_astronauts = 1
        for x in range(len(planet.items) - 1, -1, -1):
            suitable_astronauts[0].breathe()
            suitable_astronauts[0].backpack.append(planet.items[x])
            if suitable_astronauts[0].oxygen <= 0:
                count_astronauts += 1
                suitable_astronauts.pop(0)
                if not suitable_astronauts:
                    break
        else:
            self.successful_mission_count += 1
            return f"Planet: {planet_name} was explored. {count_astronauts} astronauts participated in collecting items."

        self.not_successful_mission_count += 1
        return "Mission is not completed."

    def report(self):
        output = [f"{self.successful_mission_count} successful missions!",
                  f"{self.not_successful_mission_count} missions were not completed!",
                  "Astronauts' info:"]

        for x in self.astronaut_repository.astronauts:
            output.append(f'Name: {x.name}')
            output.append(f"Oxygen: {x.oxygen}")
            output.append(f"Backpack items: " + str(', '.join(x.backpack) if x.backpack else "none"))

        return "\n".join(output)

# s = SpaceStation()
# print(s.add_astronaut("Biologist", "Ime"))
# # print(s.add_planet("ime", "asd, 123, 456"))
# # print(s.planet_repository.planets[0].items)
# # print(s.add_planet("ime", "asd, 123, 456, 321313, 123, 456, asd, 123, 456, d, 123, 456, asd, 123, 456, asd, 123, 456, asd, asd, 123, 456, asd, asd, 123, 456, asd, 123, 456, asd, 123, 456, asd, 123"))
# print(s.send_on_mission("ime"))
# print(s.retire_astronaut("Ime"))
# print(s.astronaut_repository.astronauts)
# print(s.add_astronaut("Meteorologist", "Ime"))
# print(s.astronaut_repository.find_by_name("Ime").oxygen)
# s.recharge_oxygen()
# print(s.astronaut_repository.find_by_name("Ime").oxygen)
# # print(s.planet_repository.find_by_name('ime').name)
# print(s.add_astronaut("Geodesist", 'Ime2'))
# print(s.add_astronaut("Geodesist", 'Ime3'))
# print(s.add_astronaut("Geodesist", 'Ime4'))
# print(s.add_astronaut("Geodesist", 'Ime5'))
# print(s.add_astronaut("Biologist", 'Ime6'))
# print("--------------")
# print(s.send_on_mission('ime'))
# print(s.planet_repository.find_by_name('ime').items)
# # print(s.astronaut_repository.astronauts[0].backpack)
# print("--------------------------")
# print(s.report())
# print(s.astronaut_repository.astronauts[0].backpack)

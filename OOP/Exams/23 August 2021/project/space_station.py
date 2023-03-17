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
        self.successful_missions = 0
        self.not_completed_missions = 0

    @property
    def astronauts_types(self):
        return {"Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.astronauts_types:
            raise Exception("Astronaut type is not valid!")

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        new_astronaut = self.astronauts_types[astronaut_type](name)
        self.astronaut_repository.astronauts.append(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(", "))
        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.remove(astronaut)
                return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        chosen_planet = None
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                chosen_planet = planet

        if not chosen_planet:
            raise Exception("Invalid planet name!")

        most_suitable_astronauts = []
        for astronaut in sorted(self.astronaut_repository.astronauts,key=lambda x:-x.oxygen):
            if astronaut.oxygen > 30:
                most_suitable_astronauts.append(astronaut)

        if not len(most_suitable_astronauts):
            raise Exception("You need at least one astronaut to explore the planet!")

        max_astronauts = 5
        astronauts_participated = set()
        for item in reversed(chosen_planet.items):
            if max_astronauts and len(most_suitable_astronauts):
                astronauts_participated.add(most_suitable_astronauts[0])
                most_suitable_astronauts[0].breathe()
                most_suitable_astronauts[0].backpack.append(item)

                if most_suitable_astronauts[0].oxygen <= 0:
                    most_suitable_astronauts.pop(0)
                    max_astronauts -= 1

                chosen_planet.items.pop(-1)

        if not len(chosen_planet.items):
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {len(astronauts_participated)} astronauts participated in collecting items."
        else:
            self.not_completed_missions += 1
            return "Mission is not completed."

    def report(self):
        output = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(f"Name: {astronaut.name}")
            output.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                output.append(f"Backpack items: {', '.join(str(x) for x in astronaut.backpack)}")
            else:
                output.append(f"Backpack items: none")

        return '\n'.join(output)


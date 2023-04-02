from typing import List

from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        for p in self.planets:
            if p.name == name:
                return p


from abc import ABC, abstractmethod
from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code: str = code
        self.volume: int = volume
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    @abstractmethod
    def zone_info(self):
        pass

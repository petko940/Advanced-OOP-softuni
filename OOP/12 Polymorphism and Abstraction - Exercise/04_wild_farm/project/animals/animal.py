from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    def sounds(self):
        return {"Owl": "Hoot Hoot",
                "Hen": "Cluck",
                "Mouse": "Squeak",
                "Dog": "Woof!",
                "Cat": "Meow",
                "Tiger": "ROAR!!!"}

    @property
    @abstractmethod
    def eat_type(self):
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    def feed(self, food):
        if type(food) not in self.eat_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.gained_weight
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.weight}, {self.living_region}, {self.food_eaten}]"
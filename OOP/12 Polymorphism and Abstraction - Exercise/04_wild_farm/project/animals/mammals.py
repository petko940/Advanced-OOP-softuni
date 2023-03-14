from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

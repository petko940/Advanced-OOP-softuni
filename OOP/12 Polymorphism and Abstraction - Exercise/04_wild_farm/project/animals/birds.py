from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):
    def make_sound(self):
        return self.sounds[self.__class__.__name__]

    @property
    def eat_type(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35


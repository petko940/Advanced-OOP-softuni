from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car: Car or None = None  # One driver drives ONLY one car
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Name should contain at least one character!")

        self.__name = value

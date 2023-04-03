from project.car.car import Car


class MuscleCar(Car):
    MINIMUM_SPEED_LIMIT = 250
    MAXIMUM_SPEED_LIMIT = 450

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not (self.MINIMUM_SPEED_LIMIT <= value <= self.MAXIMUM_SPEED_LIMIT):
            raise ValueError(
                f"Invalid speed limit! Must be between {self.MINIMUM_SPEED_LIMIT} and {self.MAXIMUM_SPEED_LIMIT}!")
        self.__speed_limit = value

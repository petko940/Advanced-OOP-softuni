from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > Appaloosa.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    def train(self):
        if self.speed + 2 > Appaloosa.MAXIMUM_SPEED:
            self.speed = Appaloosa.MAXIMUM_SPEED
        else:
            self.speed += 2

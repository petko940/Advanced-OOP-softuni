class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: list[object] = []

    @property
    def valid_types(self):
        return ["Winter", "Spring", "Autumn", "Summer"]

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in self.valid_types:
            raise ValueError("Race type does not exist!")

        self.__race_type = value

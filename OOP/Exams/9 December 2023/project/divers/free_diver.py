from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN = 120

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - round(0.6 * time_to_catch) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round(0.6 * time_to_catch)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN

from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption
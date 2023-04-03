from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    @property
    def valid_cars(self):
        return {"MuscleCar": MuscleCar,
                "SportsCar": SportsCar}

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.valid_cars:
            return

        try:
            next(x for x in self.cars if x.model == model)
        except StopIteration:
            new_car = self.valid_cars[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

        raise Exception(f"Car {model} is already created!")

    def create_driver(self, driver_name: str):
        try:
            next(x for x in self.drivers if x.name == driver_name)
        except StopIteration:
            new_driver = Driver(driver_name)
            self.drivers.append(new_driver)
            return f"Driver {driver_name} is created."

        raise Exception(f"Driver {driver_name} is already created!")

    def create_race(self, race_name: str):
        try:
            check = [x for x in self.races if x.name == race_name][0]
            raise Exception(f"Race {race_name} is already created!")
        except IndexError:
            new_race = Race(race_name)
            self.races.append(new_race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = next(x for x in self.drivers if x.name == driver_name)
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        cars = [x for x in self.cars if x.__class__.__name__ == car_type and not x.is_taken]
        if not cars:
            raise Exception(f"Car {car_type} could not be found!")

        car = cars[-1]
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = next(x for x in self.races if x.name == race_name)
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(x for x in self.drivers if x.name == driver_name)
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = next(x for x in self.races if x.name == race_name)
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)

        output = []
        for i in range(3):
            winners[i].number_of_wins += 1
            output.append(f"Driver {winners[i].name} wins the {race_name} "
                          f"race with a speed of {winners[i].car.speed_limit}.")

        return '\n'.join(output)

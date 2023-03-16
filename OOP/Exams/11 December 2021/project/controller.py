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
    def car_types(self):
        return {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.car_types:
            return

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        new_car = self.car_types[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    @staticmethod
    def check_if_exists(name, obj):
        for n in obj:
            if n.name == name:
                return True
        return False

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # 2
        if not self.check_if_exists(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")
        # 3
        available_car = [c for c in self.cars if c.__class__.__name__ == car_type and c.is_taken == False]
        if not available_car:  # ?????
            raise Exception(f"Car {car_type} could not be found!")
        # new
        if car_type not in ("MuscleCar", "SportsCar"):
            raise Exception(f"Car {car_type} could not be found!")

        # 5
        can_take_car = [c for c in available_car]
        # if available_car[-1]:

        new_model = can_take_car[-1]  # object
        for driver in self.drivers:
            if driver.name == driver_name:  # driver exists
                if driver.car:
                    old_model = driver.car
                    old_model.is_taken = False
                    new_model.is_taken = True
                    driver.car = new_model
                    return f"Driver {driver.name} changed his car from {old_model.model} to {new_model.model}."
                # 6
                else:
                    driver.car = new_model
                    new_model.is_taken = True
                    return f"Driver {driver_name} chose the car {new_model.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.check_if_exists(race_name, self.races):
            raise Exception(f"Race {race_name} could not be found!")

        if not self.check_if_exists(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver.car:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

        race = [r for r in self.races if r.name == race_name][0]
        for d in race.drivers:
            if driver.name == d.name:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.check_if_exists(race_name, self.races):
            raise Exception(f"Race {race_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = [drivers for drivers in race.drivers]
        result = sorted(winners, key=lambda x: -x.car.speed_limit)
        output = []
        for i in range(3):
            result[i].number_of_wins += 1
            output.append(
                f"Driver {result[i].name} wins the {race_name} race with a speed of {result[i].car.speed_limit}.")

        return '\n'.join(output)

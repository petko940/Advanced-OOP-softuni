from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @property
    def valid_horse_types(self):
        return {"Appaloosa": Appaloosa,
                "Thoroughbred": Thoroughbred}

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_types:
            return

        try:
            next(x for x in self.horses if x.name == horse_name)
        except StopIteration:
            new_horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

        raise Exception(f"Horse {horse_name} has been already added!")

    def add_jockey(self, jockey_name: str, age: int):
        try:
            next(x for x in self.jockeys if x.name == jockey_name)
        except StopIteration:
            new_jockey = Jockey(jockey_name, age)
            self.jockeys.append(new_jockey)
            return f"Jockey {jockey_name} is added."

        raise Exception(f"Jockey {jockey_name} has been already added!")

    def create_horse_race(self, race_type: str):
        try:
            next(x for x in self.horse_races if x.race_type == race_type)
        except StopIteration:
            new_race = HorseRace(race_type)
            self.horse_races.append(new_race)
            return f"Race {race_type} is created."

        raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(x for x in self.jockeys if x.name == jockey_name)
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses = [x for x in self.horses if x.__class__.__name__ == horse_type and not x.is_taken]
        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = horses[-1]
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(x for x in self.horse_races if x.race_type == race_type)
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(x for x in self.jockeys if x.name == jockey_name)
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(x for x in self.horse_races if x.race_type == race_type)
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(horse_race.jockeys, key=lambda x: -x.horse.speed)
        winner = winner[0]
        return f"The winner of the {race_type} race, " \
               f"with a speed of {winner.horse.speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."

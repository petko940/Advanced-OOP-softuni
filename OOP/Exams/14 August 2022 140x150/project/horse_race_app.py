from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    @property
    def valid_horse_types(self):
        return {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    @staticmethod
    def check_if_exists(name, obj):
        for n in obj:
            if n.name == name:
                return True
        return False

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_types:
            return

        if self.check_if_exists(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.check_if_exists(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        free_horse = []
        for horse in self.horses:
            if not horse.is_taken:
                if horse.__class__.__name__ == horse_type:
                    free_horse.append(horse)
                    break

        if not self.check_if_exists(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_jockey = [jockey for jockey in self.jockeys if jockey.name == jockey_name][0]

        if self.check_if_exists(horse_type, self.horses) or not free_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        free_horse = free_horse[-1]
        free_horse.is_taken = True
        current_jockey.horse = free_horse
        return f"Jockey {jockey_name} will ride the horse {free_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                break
        else:
            raise Exception(f"Race {race_type} could not be found!")

        if not self.check_if_exists(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_jockey = [jockey for jockey in self.jockeys if jockey.name == jockey_name][0]
        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        current_race = [race for race in self.horse_races if race.race_type == race_type][0]
        if current_jockey in current_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                current_race = race
                break
        else:
            raise f"Race {race_type} could not be found!"

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(current_race.jockeys, key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h " \
               f"is {winner.name}! Winner's horse: {winner.horse.name}."

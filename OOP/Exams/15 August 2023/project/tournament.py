from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    @property
    def valid_types_of_equipment(self):
        return {
            "KneePad": KneePad,
            "ElbowPad": ElbowPad
        }

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.valid_types_of_equipment:
            raise Exception("Invalid equipment type!")

        new_equipment = self.valid_types_of_equipment[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    @property
    def valid_types_of_teams(self):
        return {
            'OutdoorTeam': OutdoorTeam,
            'IndoorTeam': IndoorTeam,
        }

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.valid_types_of_teams:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return f"Not enough tournament capacity."

        new_team = self.valid_types_of_teams[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = None
        for equip in reversed(self.equipment):
            if equip.__class__.__name__ == equipment_type:
                equipment = equip
                break
        team = [x for x in self.teams if x.name == team_name][0]

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = [next(x for x in self.teams if x.name == team_name)][0]
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for equip in self.equipment:
            if equip.__class__.__name__ == equipment_type:
                equip.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = [x for x in self.teams if x.name == team_name1][0]
        team2 = [x for x in self.teams if x.name == team_name2][0]
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + sum(x.protection for x in team1.equipment)
        team2_points = team2.advantage + sum(x.protection for x in team2.equipment)
        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        elif team1_points < team2_points:
            team2.win()
            return f"The winner is {team2.name}."

        return f"No winner in this game."

    def get_statistics(self):
        output = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:",
        ]

        for team in sorted(self.teams, key=lambda x: -x.wins):
            output.append(team.get_statistics())

        return '\n'.join(output)

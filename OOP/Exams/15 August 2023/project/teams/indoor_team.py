from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500)

    def win(self):
        self.wins += 1
        self.advantage += 145

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self, ):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *player: Player):
        added_players = []
        for p in player:
            if p not in self.players:
                self.players.append(p)
                added_players.append(p.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supply: Supply):
        for s in supply:
            self.supplies.append(s)

    @property
    def sustenance_types(self):
        return {'Food': Food, "Drink": Drink}

    def sustain(self, player_name: str, sustenance_type: str):
        player = None
        for p in self.players:
            if p.name == player_name:
                player = p
                break

        if not player:
            return

        if sustenance_type not in self.sustenance_types:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        drinks = [d for d in self.supplies if d.__class__.__name__ == "Drink"]
        if sustenance_type == "Drink" and len(drinks) == 0:
            raise Exception("There are no drink supplies left!")

        foods = [f for f in self.supplies if f.__class__.__name__ == "Food"]
        if sustenance_type == "Food" and len(foods) == 0:
            raise Exception("There are no food supplies left!")

        supply = None
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == sustenance_type:
                supply = self.supplies.pop(i)
                break

        if player.stamina + supply.energy > 100:
            player.stamina = 100

        else:
            player.stamina += supply.energy

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        p1 = [p for p in self.players if p.name == first_player_name][0]
        p2 = [p for p in self.players if p.name == second_player_name][0]
        if p1.stamina + p2.stamina == 0:
            return f"Player {p1.name} does not have enough stamina.\n" \
                   f"Player {p2.name} does not have enough stamina.\n"
        elif p1.stamina == 0:
            return f"Player {p1.name} does not have enough stamina."
        elif p2.stamina == 0:
            return f"Player {p2.name} does not have enough stamina."

        if p1.stamina < p2.stamina:
            first, second = p1, p2
        else:
            first, second = p2, p1

        if second.stamina - first.stamina / 2 < 0:
            second.stamina = 0
            return f"Winner: {first.name}"
        else:
            second.stamina -= first.stamina / 2

        if first.stamina - second.stamina / 2 < 0:
            first.stamina = 0
            return f"Winner: {second.name}"
        else:
            first.stamina -= second.stamina / 2

        winner = sorted({first.name: first.stamina, second.name: second.stamina}.items(), key=lambda x: -x[1])
        return f"Winner: {winner[0][0]}"

    def next_day(self):
        for p in self.players:
            age = p.age * 2
            if p.stamina - age < 0:
                p.stamina = 0
            else:
                p.stamina -= age

        for p in self.players:
            for feeding in ("Food", "Drink"):
                self.sustain(p.name, feeding)

    def __str__(self):
        output = []
        [output.append(p) for p in self.players]
        [output.append(s.details()) for s in self.supplies]
        return '\n'.join(str(x) for x in output)

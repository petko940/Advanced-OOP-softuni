from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *player: Player):
        names = []
        for p in player:
            if p not in self.players:
                self.players.append(p)
                names.append(p.name)
        return f"Successfully added: {', '.join(names)}"

    def add_supply(self, *supply: Supply):
        for s in supply:
            self.supplies.append(s)

    @property
    def valid_sustenance_types(self):
        return {'Food': Food, 'Drink': Drink}

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.valid_sustenance_types:
            return

        player = [x for x in self.players if x.name == player_name]
        if not player:
            return
        player = player[0]

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        food = []
        drinks = []
        if sustenance_type == 'Food':
            for s in self.supplies:
                if s.__class__.__name__ == 'Food':
                    food.append(s)
            if not food:
                raise Exception("There are no food supplies left!")
            food = food[-1]
        elif sustenance_type == 'Drink':
            for d in self.supplies:
                if d.__class__.__name__ == 'Drink':
                    drinks.append(d)
            if not drinks:
                raise Exception("There are no drink supplies left!")
            drinks = drinks[-1]

        if sustenance_type == 'Food':
            if player.stamina + food.energy > 100:
                player.stamina = 100
            else:
                player.stamina += food.energy
            supply_name = food.name
            self.supplies.remove(food)

        else:
            if player.stamina + drinks.energy > 100:
                player.stamina = 100
            else:
                player.stamina += drinks.energy
            supply_name = drinks.name
            self.supplies.remove(drinks)

        if player.stamina > 100:
            player.stamina = 100

        return f"{player_name} sustained successfully with {supply_name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next(x for x in self.players if x.name == first_player_name)
        second_player = next(x for x in self.players if x.name == second_player_name)
        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        #       2                       1
        if first_player.stamina > second_player.stamina:
            second_player, first_player = first_player, second_player

        if second_player.stamina - first_player.stamina / 2 <= 0:
            second_player.stamina = 0
            winner = first_player
            return f"Winner: {winner.name}"
        else:
            second_player.stamina -= first_player.stamina / 2

        if first_player.stamina - second_player.stamina / 2 <= 0:
            first_player.stamina = 0
            winner = second_player
            return f"Winner: {winner.name}"
        else:
            first_player.stamina -= second_player.stamina / 2

        if first_player.stamina > second_player.stamina:
            winner = first_player
        else:
            winner = second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for p in self.players:
            if p.stamina - p.age * 2 < 0:
                p.stamina = 0
            else:
                p.stamina -= p.age * 2
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        output = []
        for p in self.players:
            output.append(p)

        for s in self.supplies:
            output.append(s.details())

        return '\n'.join(str(x) for x in output)

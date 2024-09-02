from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    def __init__(self, name: str, health: int, hit_strength: int, ):
        super().__init__(name, health, hit_strength, ammunition=80)
        self.ship_type = "PirateBattleship"

    def attack(self):
        self.ammunition -= 10

        if self.ammunition < 0:
            self.ammunition = 0

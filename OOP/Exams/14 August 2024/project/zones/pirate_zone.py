from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=8)
        self.zone_type = 'PirateZone'

    def zone_info(self):
        royal_ships = sum(1 for ship in self.get_ships() if ship.ship_type == 'RoyalBattleship')
        ship_names = ', '.join(ship.name for ship in self.ships) if self.get_ships() else ''

        output = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(self.ships)}, "
            f"{royal_ships} out of them are Royal Battleships.",
        ]

        if ship_names:
            output.append(f"#{ship_names}#")

        return '\n'.join(output)

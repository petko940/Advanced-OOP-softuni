from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)
        self.zone_type = 'RoyalZone'

    def zone_info(self):
        pirate_ships = sum(1 for ship in self.get_ships() if ship.ship_type == 'PirateBattleship')
        ship_names = ', '.join(ship.name for ship in self.get_ships()) if self.ships else ''

        output = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(self.ships)}, "
            f"{pirate_ships} out of them are Pirate Battleships.",
        ]

        if ship_names:
            output.append(f"#{ship_names}#")

        return '\n'.join(output)

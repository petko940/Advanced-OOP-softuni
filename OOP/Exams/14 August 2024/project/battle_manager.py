from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    valid_zone_types = {
        'RoyalZone': RoyalZone,
        'PirateZone': PirateZone
    }
    valid_ship_types = {
        'RoyalBattleship': RoyalBattleship,
        'PirateBattleship': PirateBattleship
    }

    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.valid_zone_types:
            raise Exception("Invalid zone type!")

        for zone in self.zones:
            if zone.code == zone_code:
                raise Exception("Zone already exists!")

        new_zone = self.valid_zone_types[zone_type](zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.valid_ship_types:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = self.valid_ship_types[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        ship_type = ship.__class__.__name__.replace("Battleship", "")
        zone_type = zone.__class__.__name__.replace("Zone", "")

        if ship_type != zone_type:
            ship.is_attacking = False
        else:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        for s in self.ships:
            if s.name == ship_name:
                ship = s
                break
        else:
            return f"No ship with this name!"

        if not ship.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacker = max((ship for ship in zone.ships if ship.is_attacking), key=lambda s: s.hit_strength, default=None)
        enemy = max((ship for ship in zone.ships if not ship.is_attacking), key=lambda s: s.health, default=None)

        if not attacker or not enemy:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        enemy.take_damage(attacker)

        if enemy.health <= 0:
            zone.ships.remove(enemy)
            self.ships.remove(enemy)
            return f"{enemy.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_battleships = [ship for ship in self.ships if ship.is_available]
        output = [f"Available Battleships: {len(available_battleships)}"]

        if available_battleships:
            output.append(f"#{', '.join([ship.name for ship in available_battleships])}#")

        output.append(f"***Zones Statistics:***")
        output.append(f"Total Zones: {len(self.zones)}")

        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda x: x.code))
        output.append(zones_info)

        return '\n'.join(output)

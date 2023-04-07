from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    @property
    def valid_types(self):
        return {"Gingerbread": Gingerbread,
                "Stolen": Stolen}

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.valid_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        try:
            next(x for x in self.delicacies if x.name == name)
            raise Exception(f"{name} already exists!")
        except StopIteration:
            new_delicacy = self.valid_types[type_delicacy](name, price)
            self.delicacies.append(new_delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    @property
    def valid_booths(self):
        return {"Open Booth": OpenBooth,
                "Private Booth": PrivateBooth}

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        try:
            next(x for x in self.booths if x.booth_number == booth_number)
            raise Exception(f"Booth number {booth_number} already exists!")
        except StopIteration:
            new_booth = self.valid_booths[type_booth](booth_number, capacity)
            self.booths.append(new_booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = next(b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved)
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(x for x in self.booths if x.booth_number == booth_number)
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(x for x in self.delicacies if x.name == delicacy_name)
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(x for x in self.booths if x.booth_number == booth_number)
        price = sum([x.price for x in booth.delicacy_orders])
        bill = booth.price_for_reservation + price

        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

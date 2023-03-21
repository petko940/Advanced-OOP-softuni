from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0

    @property
    def delicacies_types(self):
        return {"Gingerbread": Gingerbread, "Stolen": Stolen}

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for d in self.delicacies:
            if d.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.delicacies_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.delicacies_types[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    @property
    def booth_types(self):
        return {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.booth_types[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved][0]
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = [b for b in self.booths if b.booth_number == booth_number][0]
        except IndexError:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        except IndexError:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation
        for b in booth.delicacy_orders:
            bill += b.price

        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False

        self.income += bill

        output = [f"Booth {booth_number}:",
                  f"Bill: {bill:.2f}lv."]
        return '\n'.join(output)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

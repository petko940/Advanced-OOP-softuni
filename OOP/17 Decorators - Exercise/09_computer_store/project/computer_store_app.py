from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    @property
    def valid_types(self):
        return {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        new_computer = self.valid_types[type_computer](manufacturer, model)
        configure = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)
        return configure

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and \
                    computer.processor == wanted_processor and \
                    computer.ram >= wanted_ram:

                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)

                return f"{computer} sold for {client_budget}$."

        else:
            raise Exception("Sorry, we don't have a computer for you.")

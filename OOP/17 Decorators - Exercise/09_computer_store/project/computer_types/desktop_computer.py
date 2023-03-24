from math import log2

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800, }

    @property
    def max_ram(self):
        return 128

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        valid = [2 ** x for x in range(1, 8)]
        if ram not in valid or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]
        self.price += int(log2(ram)) * 100

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

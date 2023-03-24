from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_n = [x for x in System._hardware if x.name == hardware_name]
        if not hardware_n:
            return f"Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware_n[0].install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware_n = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware_n.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        software = [x for x in System._software if x.name == software_name]
        if not (hardware or software):
            return "Some of the components do not exist"

        hardware[0].uninstall(software[0])
        System._software.remove(software[0])

    @staticmethod
    def analyze():
        output = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}"]

        memory_consumption_s = sum(x.memory_consumption for x in System._software)
        memory_consumption_h = sum(x.memory for x in System._hardware)
        output.append(f"Total Operational Memory: {memory_consumption_s} / {memory_consumption_h}")
        capacity_s = sum(x.capacity_consumption for x in System._software)
        capacity_h = sum(x.capacity for x in System._hardware)
        output.append(f"Total Capacity Taken: {capacity_s} / {capacity_h}")
        return '\n'.join(output)

    @staticmethod
    def system_split():
        output = []

        for hardware in System._hardware:
            express_software = [x for x in hardware.software_components if x.__class__.__name__ == "ExpressSoftware"]
            light_software = [x for x in hardware.software_components if x.__class__.__name__ == "LightSoftware"]

            total_memory_software = sum(x.memory_consumption for x in hardware.software_components)
            total_capacity_software = sum(x.capacity_consumption for x in hardware.software_components)

            software_components = [x.name for x in hardware.software_components]

            output.append(f"Hardware Component - {hardware.name}")
            output.append(f"Express Software Components: {len(express_software)}")
            output.append(f"Light Software Components: {len(light_software)}")
            output.append(f"Memory Usage: {total_memory_software} / {hardware.memory}")
            output.append(f"Capacity Usage: {total_capacity_software} / {hardware.capacity}")
            output.append(f"Type: {hardware.hardware_type}")

            if software_components:
                output.append(f"Software Components: {', '.join(software_components)}")
            else:
                output.append("Software Components: None")

        return '\n'.join(output)

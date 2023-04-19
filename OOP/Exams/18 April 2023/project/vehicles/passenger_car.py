from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 450)

    def drive(self, mileage: float):
        percentage = round((mileage / 450) * 100)
        self.battery_level -= percentage

from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []
        self.id_route = 0

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(x for x in self.users if x.driving_license_number == driving_license_number)
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    @property
    def valid_vehicle_type(self):
        return {"PassengerCar": PassengerCar,
                "CargoVan": CargoVan}

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.valid_vehicle_type:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(x for x in self.vehicles if x.license_plate_number == license_plate_number)
            return f"{license_plate_number} belongs to another vehicle."

        except StopIteration:
            new_vehicle = self.valid_vehicle_type[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        routes = [x for x in self.routes if x.start_point == start_point and x.end_point == end_point]

        if routes:
            route = routes[0]
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                route.is_locked = True

        self.id_route += 1
        new_route = Route(start_point, end_point, length, self.id_route)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(x for x in self.users if x.driving_license_number == driving_license_number)
        vehicle = next(x for x in self.vehicles if x.license_plate_number == license_plate_number)
        route = next(x for x in self.routes if x.route_id == route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_cars = [x for x in self.vehicles if x.is_damaged]
        damaged_cars = sorted(damaged_cars, key=lambda x: (x.brand, x.model))
        count_of_repaired_vehicles = 0
        if len(damaged_cars) > count:
            for x in range(count):
                damaged_cars[x].is_damaged = False
                damaged_cars[x].battery_level = 100
                count_of_repaired_vehicles += 1
        else:
            for x in damaged_cars:
                x.is_damaged = False
                x.battery_level = 100
                count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        output = ["*** E-Drive-Rent ***"]
        for x in sorted(self.users, key=lambda x: -x.rating):
            output.append(str(x))
        return '\n'.join(output)


from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def valid_services_types(self):
        return {"MainService": MainService,
                "SecondaryService": SecondaryService}

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_services_types:
            raise Exception(f"Invalid service type!")

        new_service = self.valid_services_types[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    @property
    def valid_robot_types(self):
        return {"MaleRobot": MaleRobot,
                "FemaleRobot": FemaleRobot}

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.valid_robot_types:
            raise Exception("Invalid robot type!")

        new_robot = self.valid_robot_types[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [x for x in self.robots if x.name == robot_name][0]

        service = [x for x in self.services if x.name == service_name][0]

        if type(robot) is FemaleRobot and type(service) is not SecondaryService:
            return "Unsuitable service."
        elif type(robot) is MaleRobot and type(service) is not MainService:
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception(f"Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(x for x in self.services if x.name == service_name)

        robot = [x for x in service.robots if x.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot[0])
        self.robots.append(robot[0])
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(x for x in self.services if x.name == service_name)

        number_of_robots_fed = 0
        for x in service.robots:
            x.eating()
            number_of_robots_fed += 1
        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = next(x for x in self.services if x.name == service_name)

        total_price = 0
        for x in service.robots:
            total_price += x.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        output = []
        for service in self.services:
            output.append(service.details())

        return "\n".join(output)





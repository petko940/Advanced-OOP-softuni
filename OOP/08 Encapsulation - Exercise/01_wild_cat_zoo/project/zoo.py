from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        price = sum(s.salary for s in self.workers)
        if self.__budget >= price:
            self.__budget -= price
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        price = sum(m.money_for_care for m in self.animals)
        if self.__budget >= price:
            self.__budget -= price
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {"Lion": [], "Tiger": [], "Cheetah": []}
        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                animals["Lion"].append(str(a))
            elif a.__class__.__name__ == "Tiger":
                animals["Tiger"].append(str(a))
            else:
                animals["Cheetah"].append(str(a))

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(animals['Lion'])} Lions:",
            *animals["Lion"],
            f"----- {len(animals['Tiger'])} Tigers:",
            *animals["Tiger"],
            f"----- {len(animals['Cheetah'])} Cheetahs:",
            *animals["Cheetah"]
        ]
        return '\n'.join(result)

    def workers_status(self):
        workers = {"Keeper": [], "Caretaker": [], "Vet": []}
        [workers[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f'----- {len(workers["Keeper"])} Keepers:',
            *workers["Keeper"],
            f'----- {len(workers["Caretaker"])} Caretakers:',
            *workers["Caretaker"],
            f'----- {len(workers["Vet"])} Vets:',
            *workers["Vet"],
        ]
        return '\n'.join(result)

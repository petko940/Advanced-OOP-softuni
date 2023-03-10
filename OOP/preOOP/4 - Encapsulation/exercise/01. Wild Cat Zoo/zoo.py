class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            # self.__workers_capacity -= 1
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for x in self.workers:
            if x.name == worker_name:
                self.workers.remove(x)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum(x.salary for x in self.workers)
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_animal = sum(x.money_for_care for x in self.animals)
        if money_for_animal <= self.__budget:
            self.__budget -= money_for_animal
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = [f"You have {len(self.animals)} animals"]
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        output.append(f'----- {len(lions)} Lions:')
        [output.append(x) for x in lions]

        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        output.append(f"----- {len(tigers)} Tigers:")
        [output.append(x) for x in tigers]

        cheetahs = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]
        output.append(f'----- {len(cheetahs)} Cheetahs:')
        [output.append(x) for x in cheetahs]
        return '\n'.join(str(x) for x in output)

    def workers_status(self):
        output = [f"You have {len(self.workers)} workers"]
        keeper = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        output.append(f'----- {len(keeper)} Keepers:')
        [output.append(x) for x in keeper]

        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        output.append(f"----- {len(caretakers)} Caretakers:")
        [output.append(x) for x in caretakers]

        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        output.append(f'----- {len(vets)} Vets:')
        [output.append(x) for x in vets]
        return '\n'.join(str(x) for x in output)

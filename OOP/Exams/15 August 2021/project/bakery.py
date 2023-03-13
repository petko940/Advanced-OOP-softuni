from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu: list[BakedFood] = []
        self.drinks_menu: list[Drink] = []
        self.tables_repository: list[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @property
    def food_type(self):
        return {"Bread": Bread, "Cake": Cake}

    def add_food(self, food_type: str, name: str, price: float):
        for fm in self.food_menu:
            if fm.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.food_type:
            food = self.food_type[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    @property
    def drink_type(self):
        return {"Tea": Tea, "Water": Water}

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for dm in self.drinks_menu:
            if dm.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.drink_type:
            drink = self.drink_type[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    @property
    def table_type(self):
        return {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table_num in self.tables_repository:
            if table_num.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.table_type:
            table = self.table_type[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        current_table = [t for t in self.tables_repository if t.table_number == table_number]
        if not current_table:
            return f'Could not find table {table_number}'
        current_table = current_table[0]

        food_in_menu = [f"Table {table_number} ordered:"]
        food_not_in_menu = [f"{self.name} does not have in the menu:"]
        for food_name in food_names:
            try:
                food = [x for x in self.food_menu if x.name == food_name][0]
                food_in_menu.append(food)
                current_table.order_food(food)
            except IndexError:
                food_not_in_menu.append(food_name)

        result = food_in_menu + food_not_in_menu
        return "\n".join(str(x) for x in result)

    def order_drink(self, table_number: int, *drinks_names: str):
        current_table = [t for t in self.tables_repository if t.table_number == table_number]
        if not current_table:
            return f'Could not find table {table_number}'
        current_table = current_table[0]

        drink_in_menu = [f"Table {table_number} ordered:"]
        drink_not_in_menu = [f"{self.name} does not have in the menu:"]
        for drinks_name in drinks_names:
            try:
                drink = [x for x in self.drinks_menu if x.name == drinks_name][0]
                drink_in_menu.append(drink)
                current_table.order_drink(drink)
            except IndexError:
                drink_not_in_menu.append(drinks_name)

        result = drink_in_menu + drink_not_in_menu
        return "\n".join(str(x) for x in result)

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill

                table.clear()
                return f"Table: {table_number}\n" \
                       f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

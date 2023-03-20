from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []
        self.receipt_id = 0

    @staticmethod
    def check_is_client_registered(client_number, collection):
        for c in collection:
            if c.phone_number == client_number:
                return True
        return False

    def register_client(self, client_phone_number: str):
        if self.check_is_client_registered(client_phone_number, self.clients_list):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        show = [meal.details() for meal in self.menu]
        return '\n'.join(show)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        # menu = {}
        # for m in self.menu:
        #     menu[m.name] = m.quantity
        #
        # if len(self.menu) < 5:
        #     raise Exception("The menu is not ready!")
        #
        # if not self.check_is_client_registered(client_phone_number, self.clients_list):
        #     self.register_client(client_phone_number)
        #
        # meal_names_given, meal_names_in_menu = [], []
        #
        # for key, value in meal_names_and_quantities.items():
        #     meal_names_given.append(key)
        #     for k, v in menu.items():
        #         if k == key:
        #             if v - value < 0:
        #                 raise Exception(f"Not enough quantity of {key}: {meal_name}!")
        #
        # for meal in self.menu:
        #     meal_names_in_menu.append(meal.name)
        #
        # for meal_given in meal_names_given:
        #     if meal_given not in meal_names_in_menu:
        #         raise Exception(f"{meal_given} is not on the menu!")
        #
        # bill = 0
        # for key, value in meal_names_and_quantities.items():
        #     for meal in self.menu:
        #         if meal.name == key:
        #             meal.quantity -= value
        #             bill += meal.quantity * value
        #             client.shopping_cart.append(meal)
        #             break
        #
        # client.bill += bill
        # output_meals = []
        # for x in client.shopping_cart:
        #     output_meals.append(x.name)
        #
        # return f"Client {client_phone_number} successfully ordered {', '.join(output_meals)} for {bill:.2f}lv."
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)
        else:
            client = client[0]

        menu_meals = {}
        for m in self.menu:
            menu_meals[m.name] = [m.quantity, m.price, m]

        for meal, qty in meal_names_and_quantities.items():
            if meal not in menu_meals.keys():
                raise Exception(f"{meal} is not on the menu!")

        for meal, qty in meal_names_and_quantities.items():
            if menu_meals[meal][0] < qty:
                raise Exception(f"Not enough quantity of {menu_meals[meal][2].__class__.__name__}: {meal}!")

        current_bill = 0
        for meal, qty in meal_names_and_quantities.items():
            current_bill += qty * menu_meals[meal][1]

        for key, quantity in meal_names_and_quantities.items():
            for x in self.menu:
                if x.name == key:
                    x.quantity -= quantity
                    client.shopping_cart.append(x)
                    break

        client.bill += current_bill

        return f"Client {client_phone_number} successfully ordered {', '.join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.bill = 0
        for s in client.shopping_cart:
            for menu in self.menu:
                if s.name == menu.name:
                    menu.quantity += s.quantity
                    break

        client.shopping_cart.clear()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart.clear()
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

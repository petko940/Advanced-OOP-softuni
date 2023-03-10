class PizzaDelivery:
    def __init__(self, name, price, ingredient, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True
        prepared_by = []
        for key, value in self.ingredients.items():
            prepared_by.append(f"{key}: {value}")
        return f"You've ordered pizza {self.name} prepared with {', '.join(prepared_by)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, 1)
margarita.add_extra('123', 1, 0.5)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
print(margarita.remove_ingredient('cheese', 1, 1))
print(margarita.ordered)

from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for x in self.products:
            if x.name == product_name:
                return x

    def remove(self, product_name):
        for index, value in enumerate(self.products):
            if value.name == product_name:
                del self.products[index]

    def __repr__(self):
        output = []
        for x in self.products:
            output.append(f"{x.name}: {x.quantity}")
        return f"\n".join(output)


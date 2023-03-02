from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: [object] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product_name

    def remove(self, product_name):
        obj = self.find(product_name)
        if obj:
            self.products.remove(obj)

    def __repr__(self):
        return '\n'.join([f"{x.name}: {x.quantity}" for x in self.products])

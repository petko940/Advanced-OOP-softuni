class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @staticmethod
    def small_shop(name: str, type: str, capacity=10):
        return Shop(name, type, capacity)

    def add_item(self, item_name: str):
        if self.capacity > sum(self.items.values()):
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"

        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] - amount < 0:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Bananas", 1))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

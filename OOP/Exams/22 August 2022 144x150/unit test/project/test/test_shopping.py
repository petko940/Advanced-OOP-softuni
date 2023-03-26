import unittest

from project.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = ShoppingCart("Billa", 100)

    def test_init(self):
        self.assertEqual(self.shop.shop_name, "Billa")
        self.assertEqual(self.shop.budget, 100)
        self.assertEqual(self.shop.products, {})

    def test_shop_name_raise_property(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("qdki", 200)
        self.assertEqual(str(ve.exception), f"Product qdki cost too much!")

    def test_add_to_cart_successful(self):
        result = self.shop.add_to_cart("qdki", 2)
        self.assertEqual(result, "qdki product was successfully added to the cart!")
        result = self.shop.products
        self.assertEqual({"qdki": 2}, result)

    def test_remove_from_cart_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("sok")
        self.assertEqual(str(ve.exception), f"No product with name sok in the cart!")

    def test_remove_from_cart_successfully(self):
        self.shop.add_to_cart("bira", 2)
        self.shop.add_to_cart("vino", 5)
        result = self.shop.remove_from_cart("vino")
        self.assertEqual(result, f"Product vino was successfully removed from the cart!")

        result = self.shop.products
        self.assertEqual(result, {"bira": 2})

    def test_add_other_shop(self):
        shop1 = ShoppingCart("Billa", 100)
        shop2 = ShoppingCart("CBA", 200)
        shop1.products["bira"] = 2
        shop2.products["sok"] = 1
        new_shop = shop1 + shop2
        self.assertEqual(new_shop.shop_name, "BillaCBA")
        self.assertEqual(new_shop.budget, 300)
        self.assertEqual(new_shop.products, {"bira": 2, "sok": 1})

    def test_buy_products_raise_error(self):
        self.shop.add_to_cart("bira", 2)
        self.shop.add_to_cart("vino", 3)
        self.shop.budget = 4
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        expected = "Not enough money to buy the products! Over budget with 1.00lv!"

        self.assertEqual(str(ve.exception), expected)

    def test_buy_products_successful(self):
        self.shop.add_to_cart("bira", 2)
        self.shop.add_to_cart("vino", 3)
        self.shop.budget = 6
        expected = f'Products were successfully bought! Total cost: 5.00lv.'
        self.assertEqual(self.shop.buy_products(), expected)


if __name__ == '__main__':
    unittest.main()

import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Factory", 20)

    def test_init(self):
        self.assertEqual(self.factory.name, "Factory")
        self.assertEqual(self.factory.capacity, 20)
        self.assertEqual(self.factory.valid_ingredients, ['white', 'yellow', 'blue', 'green', 'red'])

    def test_can_add(self):
        self.assertEqual(self.factory.can_add(10), True)

    def test_add_ingredient_successfully(self):
        self.factory.add_ingredient("white", 10)
        self.assertEqual(self.factory.ingredients, {'white': 10})

    def test_add_ingredients_not_enough_space(self):
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 40)
        self.assertEqual(str(ve.exception), 'Not enough space in factory')

    def test_add_ingredients_wrong_type_raise(self):
        with self.assertRaises(Exception) as ex:
            self.factory.add_ingredient("petko", 40)
        self.assertEqual(str(ex.exception), 'Ingredient of type petko not allowed in PaintFactory')

    def test_remove_ingredient_successfully(self):
        self.factory.ingredients["white"] = 10
        self.factory.ingredients["red"] = 10
        self.assertEqual(self.factory.ingredients, {'red': 10, 'white': 10})

        self.factory.remove_ingredient('white', 5)
        self.assertEqual(self.factory.ingredients, {'red': 10, 'white': 5})

    def test_remove_ingredients_raise_value_error(self):
        self.factory.ingredients["white"] = 10
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("white", 40)
        self.assertEqual(str(ve.exception), 'Ingredients quantity cannot be less than zero')

    def test_remove_ingredients_raise_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("petko", 40)
        self.assertEqual(str(ke.exception), "'No such ingredient in the factory'")

    def test_products(self):
        self.assertEqual(self.factory.products, {})

    def test__repr__(self):
        self.factory.add_ingredient('white', 1)
        self.factory.add_ingredient('red', 3)
        self.factory.add_ingredient('blue', 4)
        expected = 'Factory name: Factory with capacity 20.\n' \
                   'white: 1\n' \
                   'red: 3\n' \
                   'blue: 4\n'
        self.assertEqual(str(self.factory), expected)


if __name__ == '__main__':
    unittest.main()

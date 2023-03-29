from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("PetShop")

    def test_init(self):
        self.assertEqual(self.pet_shop.name, "PetShop")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_add_food_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Name", -1)
        self.assertEqual(str(ve.exception), "Quantity cannot be equal to or less than 0")

    def test_add_food_if_name_not_in_food(self):
        self.assertEqual(self.pet_shop.food, {})
        self.pet_shop.add_food("Name", 10)
        self.assertEqual(self.pet_shop.food, {'Name': 10})

    def test_add_food_successfully(self):
        result = self.pet_shop.add_food("Name", 10)
        self.assertEqual(result, 'Successfully added 10.00 grams of Name.')

    def test_add_pet_successfully(self):
        result = self.pet_shop.add_pet("Dog")
        self.assertEqual(self.pet_shop.pets, ['Dog'])
        self.assertEqual(result, "Successfully added Dog.")

    def test_add_raise_exception(self):
        self.pet_shop.add_pet("Dog")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Dog")
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_feed_pet_raise_pet_is_not_in_pets(self):
        self.pet_shop.add_food("Food", 10)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Food", "Dog")
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_food_is_not_in_foods(self):
        self.pet_shop.add_pet("Dog")
        result = self.pet_shop.feed_pet("Food", "Dog")
        self.assertEqual(result, "You do not have Food")

    def test_feed_pet_food_quantity_is_lower_than_100(self):
        self.pet_shop.add_pet("Dog")
        self.pet_shop.add_food("Food", 10)
        result = self.pet_shop.feed_pet("Food", "Dog")
        self.assertEqual(result, 'Adding food...')

        self.assertEqual(self.pet_shop.food, {'Food': 1010.0})

    def test_feed_pet_successfully(self):
        self.pet_shop.add_pet("Dog")
        self.pet_shop.add_food("Food", 200)
        result = self.pet_shop.feed_pet("Food", "Dog")
        self.assertEqual(result, 'Dog was successfully fed')

        self.assertEqual(self.pet_shop.food, {'Food': 100})

    def test__repr__(self):
        self.pet_shop.add_pet("Dog")
        self.pet_shop.add_pet("Cat")
        expected = f'Shop PetShop:\n' \
                   f'Pets: Dog, Cat'

        self.assertEqual(str(self.pet_shop), expected)


if __name__ == '__main__':
    unittest.main()

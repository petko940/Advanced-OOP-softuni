from unittest import TestCase

from project.second_hand_car import SecondHandCar


class SecondHandCarTest(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar('BMW', 'Sedan', 300, 1000)
        self.car2 = SecondHandCar('Mercedes', 'Sedan', 600, 2000)
        self.car3 = SecondHandCar('Mercedes', 'Brichka', 600, 2000)

    def test__init__(self):
        self.assertEqual('BMW', self.car.model)
        self.assertEqual('Sedan', self.car.car_type)
        self.assertEqual(300, self.car.mileage)
        self.assertEqual(1000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_property_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 0
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_value_property_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(1001)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_set_new_price(self):
        self.car.set_promotional_price(200)
        self.assertEqual(200, self.car.price)
        self.assertEqual('The promotional price has been successfully set.',
                         self.car.set_promotional_price(100))

    def test_need_repair_impossible(self):
        self.car.repairs.append('Text')
        self.assertEqual('Repair is impossible!', self.car.need_repair(6000, 'Text'))
        self.assertEqual('Text', self.car.repairs[0])

    def test_need_repair_successful(self):
        self.car.price = 2000
        repair_price = self.car.price / 2
        self.car.need_repair(repair_price, 'Text')
        self.assertEqual(3000, self.car.price)
        self.assertEqual('Text', self.car.repairs[0])
        self.assertEqual(1, len(self.car.repairs))
        self.car.need_repair(100, "Repair")
        self.assertEqual(3100, self.car.price)
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(100, "Repair"))

    def test__gt__car1_different_than_car2(self):
        result = self.car > self.car3
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test__gt__car1_different_than_car2_2(self):
        self.assertEqual(False, self.car > self.car2)

    def test___gt__car2_price_higher_than_car1(self):
        self.assertEqual(False, self.car.price > self.car2.price)

    def test__str__(self):
        self.assertEqual('''Model BMW | Type Sedan | Milage 300km
Current price: 1000.00 | Number of Repairs: 0''',
                         str(self.car))

        self.car2.repairs.append('Text')
        self.assertEqual('''Model Mercedes | Type Sedan | Milage 600km
Current price: 2000.00 | Number of Repairs: 1''', str(self.car2))


if __name__ == '__main__':
    TestCase()

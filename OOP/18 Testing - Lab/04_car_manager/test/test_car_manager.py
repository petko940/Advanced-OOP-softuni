import unittest

# from project.car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("make", "lada", 20, 20)

    def test_make_attr(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        result = ex.exception
        self.assertEqual(str(result), "Make cannot be null or empty!")

    def test_model_attr(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        result = ex.exception
        self.assertEqual(str(result), "Model cannot be null or empty!")

    def test_fuel_consumption_attr(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        result = ex.exception
        self.assertEqual(str(result), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_attr(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        result = ex.exception
        self.assertEqual(str(result), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_attr(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        result = ex.exception
        self.assertEqual(str(result), "Fuel amount cannot be negative!")

    def test_refuel_fuel_lower_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        result = ex.exception
        self.assertEqual(str(result), "Fuel amount cannot be zero or negative!")

    def test_refuel_fuel_more_than_amount(self):
        self.car.refuel(30)
        result = self.car.fuel_amount
        expected = 20
        self.assertEqual(result, expected)

    def test_drive_not_successful(self):
        self.car.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)  # 20
        result = ex.exception
        self.assertEqual(str(result), "You don't have enough fuel to drive!")

    def test_drive_successful(self):
        self.car.fuel_amount = 10
        self.car.drive(20)
        result = self.car.fuel_amount - 20 / 100 * self.car.fuel_consumption
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

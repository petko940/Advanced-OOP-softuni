import unittest

from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver('Petko', 10)

    def test_init(self):
        self.assertEqual(self.driver.name, "Petko")
        self.assertEqual(self.driver.money_per_mile, 10)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_raise_value(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(str(ve.exception), "Petko went bankrupt.")

    def test_add_cargo_offer_raise_exception(self):
        self.driver.available_cargos["burgas"] = 10
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("burgas", 20)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_successfully(self):
        result = self.driver.add_cargo_offer("burgas", 20)
        self.assertEqual(result, "Cargo for 20 to burgas was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {'burgas': 20})

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.1
        self.driver.add_cargo_offer("Varna", 100_000)
        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_drive_best_cargo_offer_not_successfully(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer_successfully(self):
        self.driver.earned_money = 999_999
        self.driver.add_cargo_offer("burgas", 20)
        self.driver.add_cargo_offer("varna", 10)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Petko is driving 20 to burgas.")
        self.assertEqual(self.driver.earned_money, 1000199)
        self.assertEqual(self.driver.miles, 20)
        self.driver.check_for_activities(10000)

    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1100)
        result = self.driver.earned_money
        self.assertEqual(result, 875)

    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.check_for_activities(1100)
        result = self.driver.earned_money
        self.assertEqual(result, 875)

    def test_pump_gas(self):
        self.driver.earned_money = 1500
        self.driver.check_for_activities(1501)
        result = self.driver.earned_money
        self.assertEqual(result, 835)

    def test_repair_truck(self):
        self.driver.earned_money = 100_000
        self.driver.check_for_activities(10000)
        result = self.driver.earned_money
        self.assertEqual(result, 88250)

    def test_check_all_activities(self):
        self.driver.earned_money = 100_000
        self.driver.check_for_activities(20_000)
        result = self.driver.earned_money
        self.assertEqual(result, 76000)

    def test_repr_(self):
        result = str(self.driver)
        self.assertEqual(result, "Petko has 0 miles behind his back.")


if __name__ == '__main__':
    unittest.main()

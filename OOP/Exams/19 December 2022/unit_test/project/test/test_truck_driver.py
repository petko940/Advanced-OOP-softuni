from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = TruckDriver("Bai Ivan", 10)

    # def test_init(self):
    #     self.assertEqual(self.truck.name, "Bai Ivan")
    #     self.assertEqual(self.truck.money_per_mile, 10)
    #     self.assertEqual(self.truck.available_cargos, {})
    #     self.assertEqual(self.truck.earned_money, 0)
    #     self.assertEqual(self.truck.miles, 0)

    def test_earned_money_init_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck.earned_money = -1
        result = ve.exception
        self.assertEqual(str(result), "Bai Ivan went bankrupt.")

    def test_bankrupt(self):
        self.truck.money_per_mile = 0.01
        self.truck.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.truck.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.truck.name} went bankrupt.")

    def test_add_cargo_offer_raise_exception(self):
        self.truck.available_cargos["Burgas"] = 10
        with self.assertRaises(Exception) as ex:
            self.truck.add_cargo_offer("Burgas", 10)
        result = ex.exception
        self.assertEqual(str(result), "Cargo offer is already added.")

    def test_add_cargo_offer_successful(self):
        result = self.truck.add_cargo_offer("Burgas", 5)
        self.assertEqual(result, "Cargo for 5 to Burgas was added as an offer.")
        self.assertEqual({"Burgas": 5}, self.truck.available_cargos)

        # result2 = self.truck.add_cargo_offer("Varna", 10)
        # self.assertEqual(result2, "Cargo for 10 to Varna was added as an offer.")
        # self.assertEqual({"Burgas": 5, "Varna": 10}, self.truck.available_cargos)
        # self.assertEqual(len(self.truck.available_cargos), 2)

    def test_drive_best_cargo_offer_return(self):
        self.truck.earned_money = 100_000

        self.truck.available_cargos["Burgas"] = 5
        self.truck.available_cargos["Varna"] = 10

        result = self.truck.drive_best_cargo_offer()
        self.assertEqual(str(result), "Bai Ivan is driving 10 to Varna.")

        self.assertEqual(self.truck.earned_money, 100_100)
        self.assertEqual(self.truck.miles, 10)
        self.truck.check_for_activities(10000)

    def test_drive_best_cargo_offer_raise(self):
        self.assertEqual(self.truck.drive_best_cargo_offer(), "There are no offers available.")

    # def test_call_activities_methods(self):
    #     self.test_check_for_activities_eat()
    #     self.test_check_for_activities_sleep()
    #     self.test_check_for_activities_pump_gas()
    #     self.test_check_for_activities_repair_truck()

    def test_check_for_activities_eat(self):
        self.truck.earned_money = 100
        self.truck.check_for_activities(250)
        expected = 80
        self.assertEqual(self.truck.earned_money, expected)

    def test_check_for_activities_sleep(self):
        self.truck.earned_money = 1000
        self.truck.check_for_activities(1000)
        expected = 875
        self.assertEqual(self.truck.earned_money, expected)

    def test_check_for_activities_pump_gas(self):
        self.truck.earned_money = 1000
        self.truck.check_for_activities(1500)
        expected = 335
        self.assertEqual(self.truck.earned_money, expected)

    def test_check_for_activities_repair_truck(self):
        self.truck.earned_money = 100_000
        self.truck.check_for_activities(100_00)
        expected = 88250
        self.assertEqual(self.truck.earned_money, expected)

    def test_truck_driver(self):
        result = self.truck.__repr__()
        self.assertEqual(result, "Bai Ivan has 0 miles behind his back.")


if __name__ == '__main__':
    unittest.main()

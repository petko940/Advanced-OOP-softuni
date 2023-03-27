from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20, 100)

    def test_cls_attributes(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 20)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_successful(self):
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, 13.75)

    def test_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_successful(self):
        self.vehicle.fuel -= 10
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 11)

    def test_str(self):
        expected = "The vehicle has 100 " \
                   f"horse power with 20 fuel left and 1.25 fuel consumption"
        self.assertEqual(str(self.vehicle), expected)


if __name__ == '__main__':
    main()

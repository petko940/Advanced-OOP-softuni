from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1337", "Military", 30, 100)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, "1337")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 30)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)

    def test_category_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Cat1"
        self.assertEqual(str(ve.exception),
                         "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -100
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_not_successful(self):
        self.robot.hardware_upgrades.append('hardware1')
        result = self.robot.upgrade("hardware1", 100)
        self.assertEqual(result, "Robot 1337 was not upgraded.")

    def test_upgrade_successful(self):
        result = self.robot.upgrade("hardw1", 100)
        self.assertEqual(result, 'Robot 1337 was upgraded with hardw1.')
        self.assertEqual(self.robot.hardware_upgrades, ['hardw1'])
        self.assertEqual(self.robot.price, 250)

    def test_update_not_successful(self):
        self.robot.software_updates.append(100)
        self.robot.software_updates.append(1000)
        self.robot.software_updates.append(10000)
        result = self.robot.update(1001, 20)
        self.assertEqual(result, "Robot 1337 was not updated.")

        result = self.robot.update(12, 50)
        self.assertEqual(result, "Robot 1337 was not updated.")

    def test_update_successful(self):
        self.robot.software_updates.append(100)
        self.robot.software_updates.append(1000)
        self.robot.software_updates.append(10000)
        result = self.robot.update(100_000, 20)
        self.assertEqual(result, 'Robot 1337 was updated to version 100000.')

        self.assertEqual(self.robot.software_updates, [100, 1000, 10000, 100000])
        self.assertEqual(self.robot.available_capacity, 10)

    def test_gt_first(self):
        other = Robot("1336", 'Education', 23, 80)
        self.assertEqual(self.robot.__gt__(other), "Robot with ID 1337 is more expensive than Robot with ID 1336.")

    def test_gt_second(self):
        other = Robot("1336", 'Education', 23, 100)
        self.assertEqual(self.robot.__gt__(other), 'Robot with ID 1337 costs equal to Robot with ID 1336.')

    def test_gt_last(self):
        other = Robot("1336", 'Education', 23, 120)
        self.assertEqual(self.robot.__gt__(other), 'Robot with ID 1337 is cheaper than Robot with ID 1336.')


if __name__ == '__main__':
    main()

import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train("Vlak", 100)

    def test_class_attributes(self):
        self.assertEqual(Train.TRAIN_FULL, "Train is full")
        self.assertEqual(Train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(Train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(Train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(Train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(Train.ZERO_CAPACITY, 0)

    def test_init(self):
        self.assertEqual(self.train.name, 'Vlak')
        self.assertEqual(self.train.capacity, 100)
        self.assertEqual(self.train.passengers, [])

    def test_add_raise_value_error(self):
        self.train.passengers = ["Petko"]
        self.train.capacity = 1
        with self.assertRaises(ValueError) as ve:
            self.train.add("Petko")
        self.assertEqual(str(ve.exception), 'Train is full')

    def test_add_passenger_exists(self):
        self.train.passengers = ["Petko"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Petko")
        self.assertEqual(str(ve.exception), 'Passenger Petko Exists')

    def test_add_passenger_successfully(self):
        result = self.train.add("Petko")
        self.assertEqual(result, 'Added passenger Petko')
        self.assertEqual(self.train.passengers, ['Petko'])

    def test_remove_passenger_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove('Petko')
        self.assertEqual(str(ve.exception), 'Passenger Not Found')

    def test_remove_passenger_successfully(self):
        self.train.add("Petko")
        result = self.train.remove("Petko")
        self.assertEqual(result, "Removed Petko")


if __name__ == '__main__':
    unittest.main()

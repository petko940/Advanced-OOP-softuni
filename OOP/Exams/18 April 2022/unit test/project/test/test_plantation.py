from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -10
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_raise_value_error(self):
        self.plantation.workers.append("Petko")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Petko")
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Petko")
        self.assertEqual(result, "Petko successfully hired.")
        self.assertEqual(self.plantation.workers, ['Petko'])

    def test__len__(self):
        self.plantation.plants["Petko"] = ['plant1', 'plant2']
        self.plantation.plants["Ivan"] = ["plant2"]
        self.plantation.plants["Georgi"] = ['plant3']
        self.assertEqual(len(self.plantation), 4)

    def test_planting_missing_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Vankata", "plant")
        self.assertEqual(str(ve.exception), "Worker with name Vankata is not hired!")

    def test_planting_len_bigger_than_size(self):
        self.plantation.size = 1
        self.plantation.hire_worker('Petko')
        self.plantation.plants["Petko"] = ['plant1', 'plant2']
        self.plantation.plants["Ivan"] = ["plant2"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Petko", "plant15")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_plant_not_first_plant(self):
        self.plantation.hire_worker('Petko')
        self.plantation.plants["Petko"] = ['plant1', 'plant2']
        result = self.plantation.planting('Petko', "plant5")
        self.assertEqual(result, "Petko planted plant5.")
        self.assertEqual(self.plantation.plants['Petko'], ['plant1', 'plant2', 'plant5'])

    def test_planting_plant_first_plant(self):
        self.plantation.hire_worker('Petko')
        result = self.plantation.planting('Petko', "plant5")
        self.assertEqual(result, "Petko planted it's first plant5.")
        self.assertEqual(self.plantation.plants['Petko'], ['plant5'])

    def test__str__(self):
        self.plantation.hire_worker("Petko")
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Petko", "plant")
        self.plantation.planting("Petko", "plant1")
        self.plantation.planting("Ivan", "plant2")
        self.assertEqual(str(self.plantation), "Plantation size: 10\n"
                                               "Petko, Ivan\n"
                                               "Petko planted: plant, plant1\n"
                                               "Ivan planted: plant2")

    def test__repr__(self):
        self.plantation.hire_worker("Petko")
        self.plantation.hire_worker("Ivan")
        self.plantation.planting("Petko", "plant")
        self.plantation.planting("Petko", "plant1")
        self.plantation.planting("Ivan", "plant2")
        self.assertEqual(self.plantation.__repr__(), "Size: 10\n"
                                                     "Workers: Petko, Ivan")


if __name__ == '__main__':
    main()

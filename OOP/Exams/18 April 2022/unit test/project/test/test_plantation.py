import unittest

from project.plantation import Plantation


class TestPlantation(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(4)
        self.plantation.plants = {"Ivan": ["cvete1", "cvete2"],
                                  "Petko": ["cvete3"], }
        self.plantation.workers = ["Ivan", "Petko"]

    def test_size_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -10
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_already_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_worker_successful(self):
        result = self.plantation.hire_worker("Gosho")
        self.assertEqual(result, "Gosho successfully hired.")

        result = self.plantation.workers
        self.assertEqual(result, ['Ivan', 'Petko', 'Gosho'])

    def test_len_plants_dict(self):
        result = len(self.plantation)
        self.assertEqual(result, 3)
        # ??

    def test_planting_worker_not_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "cvete1")

        self.assertEqual(str(ve.exception), "Worker with name Gosho is not hired!")

    def test_planting_raise_error_number_plant(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.plants["Petko"] = ["cvete5", "cvete6", ]
            self.plantation.planting("Petko", "cvete8")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_more_plants(self):
        result = self.plantation.planting("Petko", "cvete4")
        self.assertEqual(result, "Petko planted cvete4.")

        self.assertEqual(len(self.plantation.plants["Petko"]), 2)

    def test_planting_first_plant(self):
        self.plantation.hire_worker("Vanko1")
        result = self.plantation.planting("Vanko1", "cvete1")
        self.assertEqual(result, "Vanko1 planted it's first cvete1.")
        self.assertEqual(self.plantation.plants["Vanko1"], ["cvete1"])

    def test_str(self):
        expected = "Plantation size: 4\n" \
                   "Ivan, Petko\n" \
                   "Ivan planted: cvete1, cvete2\n" \
                   "Petko planted: cvete3"
        self.assertEqual(str(self.plantation), expected)

    def test_repr(self):
        expected = "Size: 4\n" \
                   "Workers: Ivan, Petko"
        self.assertEqual(self.plantation.__repr__(), expected)


if __name__ == '__main__':
    unittest.main()

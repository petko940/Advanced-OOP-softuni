import unittest

from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual(self.store.toy_shelf,
                         {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None})

    def test_add_toy_shelf_dont_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "toy")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_already_on_shelf(self):
        self.store.toy_shelf["A"] = 'toy'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", 'toy')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        self.store.toy_shelf["A"] = 'toy'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", 'ball')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_successfully(self):
        result = self.store.add_toy("A", 'toy')
        self.assertEqual(result, "Toy:toy placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], 'toy')

    def test_remove_toy_shelf_dont_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", 'toy')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_dont_exist(self):
        self.store.add_toy("A", 'toy')
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", 'Toy')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.store.add_toy("A", 'toy')
        self.assertEqual(self.store.toy_shelf["A"], 'toy')
        result = self.store.remove_toy("A", 'toy')
        self.assertEqual(result, 'Remove toy:toy successfully!')
        self.assertEqual(self.store.toy_shelf["A"], None)


if __name__ == '__main__':
    unittest.main()

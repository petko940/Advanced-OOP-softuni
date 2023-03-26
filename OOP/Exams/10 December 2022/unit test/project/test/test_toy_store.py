import unittest

from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_add_toy_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "igrachka")
        result = ex.exception
        self.assertEqual(str(result), "Shelf doesn't exist!")

    def test_add_toy_is_in_shelf(self):
        self.store.toy_shelf["A"] = "ball"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "ball")
        result = ex.exception
        self.assertEqual(str(result), "Toy is already in shelf!")

    def test_add_toy_shelf_is_taken(self):
        self.store.toy_shelf["A"] = "ball"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "neshto")
        result = ex.exception
        self.assertEqual(str(result), "Shelf is already taken!")

    def test_add_successful(self):
        # self.store.add_toy("A", "ball")
        # self.store.add_toy("B", "ball")
        # result = self.store.toy_shelf["A"]
        # self.assertEqual(result, "ball")
        # self.assertEqual(self.store.toy_shelf["B"], "ball")
        # result = self.store.add_toy("A", "Car")
        # self.assertEqual(result, "Toy:Car placed successfully!")
        # self.assertEqual(self.store.toy_shelf["A"], "Car")
        pass

    def test_add_toy_return(self):
        result = self.store.add_toy("A", "ball")
        expect = f"Toy:ball placed successfully!"
        self.assertEqual(result, expect)

        self.assertEqual(self.store.toy_shelf["A"], "ball")


    def test_remove_toy_if_shelf_exists(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "ball")
        result = ex.exception
        self.assertEqual(str(result), "Shelf doesn't exist!")

    def test_remove_toy_if_toy_exists(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "igrachka")
        result = ex.exception
        self.assertEqual(str(result), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successful(self):
        self.store.toy_shelf["A"] = "ball"
        self.store.remove_toy("A", "ball")

        self.assertEqual(self.store.toy_shelf["A"], None)

    def test_remove_toy_successful_return_text(self):
        self.store.toy_shelf["A"] = "ball"
        resul = self.store.remove_toy("A", "ball")
        self.assertEqual(resul, "Remove toy:ball successfully!")


if __name__ == '__main__':
    unittest.main()

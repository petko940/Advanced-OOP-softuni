import unittest
# from project.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, 1.1, "test")

    def test_init(self):
        result = [1, 2, 3]
        expected = self.integer_list._IntegerList__data
        self.assertEqual(result, expected)

    def test_get_data(self):
        result = [1, 2, 3]
        expected = self.integer_list.get_data()
        self.assertEqual(result, expected)

    def test_fail_add(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("1")
        result = ve.exception
        expected = "Element is not Integer"
        self.assertEqual(str(result), expected)

    def test_add(self):
        self.integer_list.add(4)
        result = self.integer_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4])

    def test_fail_remove_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)
        result = ie.exception
        expected = "Index is out of range"
        self.assertEqual(str(result), expected)

    def test_remove_index_successful(self):
        result = self.integer_list.remove_index(2)
        self.assertEqual(result, 3)

    def test_fail_get_method(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)
        result = ie.exception
        self.assertEqual(str(result), "Index is out of range")

    def test_successful_get(self):
        result = self.integer_list.get(0)
        self.assertEqual(result, 1)
        self.assertEqual(result, self.integer_list._IntegerList__data[0])

    def test_get_biggest(self):
        a = self.integer_list.get_biggest()
        self.assertEqual(a, 3)

    def test_fail_insert_index_error_method(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(100, 1)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_fail_insert_value_error_method(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, "test")
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_successful_insert(self):
        self.integer_list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_index(self):
        a = self.integer_list.get_index(1)
        self.assertEqual(a, 0)


if __name__ == '__main__':
    unittest.main()

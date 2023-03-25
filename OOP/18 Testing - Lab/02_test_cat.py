class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_cat_size_increase_after_eat(self):
        self.cat.eat()
        result = self.cat.size
        expected = 1
        self.assertEqual(result, expected)

    def test_cat_if_fed_after_eat(self):
        self.cat.eat()
        result = self.cat.fed
        expected = True
        self.assertTrue(result, expected)

    def test_cat_cant_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as text:
            self.cat.eat()
        result = text.exception
        expected = 'Already fed.'
        self.assertEqual(str(result), expected)

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as text:
            self.cat.sleep()
        result = text.exception
        expected = 'Cannot sleep while hungry'
        self.assertEqual(str(result), expected)

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        result = self.cat.sleepy
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

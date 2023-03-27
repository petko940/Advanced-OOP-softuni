import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Buch", "dog", "bau")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Buch")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bau")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Buch makes bau")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        expected = "Buch is of type dog"
        self.assertEqual(self.mammal.info(), expected)


if __name__ == '__main__':
    unittest.main()

from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Biblioteka")

    def test_init(self):
        self.assertEqual(self.library.name, "Biblioteka")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_author_not_in_library(self):
        self.assertEqual(self.library.books_by_authors, {})
        self.library.add_book("Petko", "Kniga")
        self.assertEqual(self.library.books_by_authors, {'Petko': ['Kniga']})

    def test_add_book_title_not_in_library(self):
        self.library.books_by_authors["Petko"] = ["Kniga"]
        self.assertEqual(self.library.books_by_authors['Petko'], ['Kniga'])

        self.library.add_book("Petko", "Kniga2")
        self.assertEqual(self.library.books_by_authors, {'Petko': ['Kniga', 'Kniga2']})

    def test_add_reader_is_not_in_readers(self):
        self.assertEqual(self.library.readers, {})

        self.library.add_reader("Petko")
        self.assertEqual(self.library.readers, {'Petko': []})

    def test_add_reader_already_registered(self):
        self.library.readers["Petko"] = []
        result = self.library.add_reader("Petko")
        self.assertEqual(result, "Petko is already registered in the Biblioteka library.")

    def test_rent_book_reader_not_registered(self):
        result = self.library.rent_book("Petko", "Ivan", "Kniga")
        self.assertEqual(result, "Petko is not registered in the Biblioteka Library.")

    def test_rent_book_author_dont_have_book(self):
        self.library.add_reader("Petko")
        result = self.library.rent_book("Petko", "Ivan", "Kniga1")
        self.assertEqual(result, "Biblioteka Library does not have any Ivan's books.")

    def test_rent_book_title_missing(self):
        self.library.add_reader("Petko")
        self.library.add_book("Ivan", "Kniga")
        result = self.library.rent_book("Petko", "Ivan", "Kniga1")
        self.assertEqual(result, """Biblioteka Library does not have Ivan's "Kniga1".""")

    def test_rent_book_successful(self):
        self.library.add_reader("Petko")
        self.library.add_book("Ivan", "Kniga")
        self.library.rent_book("Petko", "Ivan", "Kniga")
        self.assertEqual(self.library.readers["Petko"], [{'Ivan': 'Kniga'}])
        self.assertEqual(self.library.books_by_authors, {'Ivan': []})


if __name__ == '__main__':
    unittest.main()

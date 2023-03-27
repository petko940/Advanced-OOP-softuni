from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self) -> None:
        self.books = Bookstore(10)

    def test_init(self):
        self.assertEqual(self.books.books_limit, 10)
        self.assertEqual(self.books.availability_in_store_by_book_titles, {})
        self.assertEqual(self.books.total_sold_books, 0)

    def test_books_limit_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.books.books_limit = 0
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_books_limit_successful(self):
        self.assertEqual(self.books.books_limit, 10)

    def test_count_total_books(self):
        self.books.availability_in_store_by_book_titles = {
            "book1": 2,
            "book2": 3,
        }
        self.assertEqual(len(self.books), 5)

    def test_receive_book_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.books.receive_book("book1", 20)
        result = ex.exception
        self.assertEqual(str(result), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_if_enough_space(self):
        self.books.receive_book("book1", 1)
        self.books.receive_book("book2", 2)
        self.books.receive_book("book3", 3)
        expected = {'book1': 1, 'book2': 2, 'book3': 3}
        self.assertEqual(self.books.availability_in_store_by_book_titles,
                         expected)

    def test_receive_book_successful(self):
        self.books.receive_book("book1", 1)
        result = self.books.receive_book("book1", 2)
        self.assertEqual(result, "3 copies of book1 are available in the bookstore.")

    def test_sell_book_if_book_not_available(self):
        self.books.availability_in_store_by_book_titles = {"book2 : 2"}

        with self.assertRaises(Exception) as ex:
            self.books.sell_book("book1", 1)
        result = ex.exception
        self.assertEqual(str(result), "Book book1 doesn't exist!")

    def test_sell_book_if_book_number_not_enough(self):
        self.books.availability_in_store_by_book_titles = {"book1": 2}

        with self.assertRaises(Exception) as ex:
            self.books.sell_book("book1", 3)
        result = ex.exception
        self.assertEqual(str(result), "book1 has not enough copies to sell. Left: 2")

    def test_sell_book_successful(self):
        self.books.receive_book("book1", 5)
        result = self.books.sell_book("book1", 1)
        self.assertEqual(result, "Sold 1 copies of book1")
        self.assertEqual(self.books.total_sold_books, 1)
        self.assertEqual(self.books.availability_in_store_by_book_titles["book1"], 4)

        self.books.receive_book("book2", 2)
        result = self.books.sell_book("book2", 2)
        self.assertEqual(result, "Sold 2 copies of book2")

        self.assertEqual(self.books.availability_in_store_by_book_titles, {'book1': 4, 'book2': 0})
        self.assertEqual(self.books.total_sold_books, 3)

    def test_bookstore_str(self):
        self.books.receive_book("book1", 1)
        self.books.receive_book("book2", 2)

        expected = "Total sold books: 0\n" \
                   "Current availability: 3\n" \
                   " - book1: 1 copies\n" \
                   " - book2: 2 copies"
        self.assertEqual(str(self.books), expected)


if __name__ == '__main__':
    unittest.main()

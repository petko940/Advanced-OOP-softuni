import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("film", 2000, 8)
        self.movie2 = Movie("film2", 2002, 6)

    def test_init(self):
        self.assertEqual(self.movie.name, "film")
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 8)
        self.assertEqual(self.movie.actors, [])

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_not_in_actors(self):
        self.movie.add_actor("Petko")
        self.assertEqual(self.movie.actors, ['Petko'])

    def test_add_actor_already_in_actors(self):
        self.movie.actors.append("Petko")
        result = self.movie.add_actor("Petko")
        self.assertEqual(result, 'Petko is already added in the list of actors!')

    def test_first_movie_greater_rating_than_other(self):
        result = self.movie.__gt__(self.movie2)
        self.assertEqual(result, '"film" is better than "film2"')

    def test_other_movie_greater_rating_than_first(self):
        self.movie.rating, self.movie2.rating = self.movie2.rating, self.movie.rating
        result = self.movie.__gt__(self.movie2)
        self.assertEqual(result, '"film2" is better than "film"')

    def test_repr(self):
        self.movie.add_actor("Petko")
        expected = f"Name: film\n" \
                   f"Year of Release: 2000\n" \
                   f"Rating: 8.00\n" \
                   f"Cast: Petko"
        self.assertEqual(str(self.movie), expected)


if __name__ == '__main__':
    unittest.main()

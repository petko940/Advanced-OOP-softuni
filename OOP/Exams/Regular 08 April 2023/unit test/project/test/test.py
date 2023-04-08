from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Petko", 28, 0)
        self.player2 = TennisPlayer("Ivan", 20, 2000)

    # def test_init(self):
    #     self.assertEqual(self.player.name, "Petko")
    #     self.assertEqual(self.player.age, 28)
    #     self.assertEqual(self.player.points, 0.0)
    #     self.assertEqual(self.player.wins, [])
    #
    #     self.player2.wins = ["won1", "won2"]
    #     self.assertEqual(self.player2.name, "Ivan")
    #     self.assertEqual(self.player2.age, 20)
    #     self.assertEqual(self.player2.points, 2000)
    #     self.assertEqual(self.player2.wins, ['won1', 'won2'])

    def test_create_player_with_valid_name(self):
        player = TennisPlayer("Petko", 34, 12000)
        self.assertEqual(player.name, "Petko")

    def test_name_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Pe"
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_name_raise_again(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = ""
        self.assertEqual(str(ve.exception), 'Name should be more than 2 symbols!')

    def test_age_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 10
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_tournament_not_in_wins(self):
        self.player.add_new_win("turnir")
        self.assertEqual(self.player.wins, ['turnir'])

    def test_add_new_win_tournament_in_wins(self):
        self.player.add_new_win("turnir")
        self.player.add_new_win("turnir2")
        self.assertEqual(self.player.wins, ['turnir', 'turnir2'])
        result = self.player.add_new_win("turnir")
        self.assertEqual(result, 'turnir has been already added to the list of wins!')

    def test__lt__(self):
        self.assertEqual(self.player.__lt__(self.player2), "Ivan is a top seeded player and he/she is better than Petko")
        self.assertEqual(self.player2.__lt__(self.player),
                         "Ivan is a better player than Petko")

    def test__str__(self):
        self.player.add_new_win("win1")
        self.player.add_new_win("win2")
        result = str(self.player)

        self.assertEqual(result, "Tennis Player: Petko\n"
                                 "Age: 28\n"
                                 "Points: 0.0\n"
                                 "Tournaments won: win1, win2")


if __name__ == '__main__':
    main()

from project.team import Team
import unittest


class TestTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team("TeamOne")
        self.team2 = Team("TeamTwo")

    def test_init(self):
        self.assertEqual(self.team.name, "TeamOne")
        self.assertEqual(self.team.members, {})

    def test_incorrect_name(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'Team1'
        self.assertEqual(str(ve.exception), 'Team Name can contain only letters!')

    def test_member(self):
        result = self.team.add_member(Petko=28, Ivan=25)
        self.assertEqual(result, 'Successfully added: Petko, Ivan')
        self.assertEqual(self.team.members, {'Ivan': 25, 'Petko': 28})

    def test_remove_member_successfully(self):
        self.team.add_member(Petko=28, Ivan=25)
        result = self.team.remove_member('Ivan')
        self.assertEqual(result, 'Member Ivan removed')
        self.assertEqual(self.team.members, {'Petko': 28})

    def test_remove_member_not_exists(self):
        self.team.add_member(Petko=28)
        result = self.team.remove_member('Ivan')
        self.assertEqual(result, 'Member with name Ivan does not exist')

    def test__gt__(self):
        self.team.add_member(Petko=28, Ivan=25)
        self.team2.add_member(Gosho=29)
        self.assertEqual(self.team.__gt__(self.team2), True)

    def test__gt__false(self):
        self.team.add_member(Petko=28)
        self.team2.add_member(Gosho=29, Ivan=24)
        self.assertEqual(self.team.__gt__(self.team2), False)

    def test__len__(self):
        self.team.add_member(Petko=28)
        result = self.team.__len__()
        self.assertEqual(result, 1)

        self.team.add_member(Gosho=30)
        result = self.team.__len__()
        self.assertEqual(result, 2)

    def test__add__(self):
        team1 = Team('TeamOne')
        team1.add_member(Petko=28, Ivan=28)
        team1.remove_member("Petko")
        team2 = Team('TeamTwo')
        team2.add_member(Gosho=29)
        new_team = team1 + team2
        self.assertEqual(new_team.name, 'TeamOneTeamTwo')
        self.assertEqual(new_team.members, {'Gosho': 29, 'Ivan': 28})

    def test__str__(self):
        self.team.add_member(Petko=28, Ivan=25)
        result = str(self.team)
        self.assertEqual(result, 'Team name: TeamOne\n'
                                 'Member: Petko - 28-years old\n'
                                 'Member: Ivan - 25-years old')

        self.team2.add_member(Petko=21)
        result = str(self.team2)
        self.assertEqual(result, 'Team name: TeamTwo\n'
                                 'Member: Petko - 21-years old')


if __name__ == '__main__':
    unittest.main()

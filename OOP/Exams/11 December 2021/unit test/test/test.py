from project.team import Team
import unittest


class TestTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")
        self.team2 = Team("TeamTwo")

    def test_init(self):
        self.assertEqual(self.team.name, "Team")
        self.assertEqual(self.team.members, {})

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "test1"
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member_successfully(self):
        result = self.team.add_member(Petko=28, Ivan=24)
        self.assertEqual(result, "Successfully added: Petko, Ivan")
        self.assertEqual(self.team.members, {'Ivan': 24, 'Petko': 28})
        self.assertEqual(len(self.team.members), 2)
        result = self.team.add_member(Petko=30)
        self.assertEqual(result, "Successfully added: ")

    def test_remove_member_successfully(self):
        self.team.add_member(Petko=28, Ivan=24)
        result = self.team.remove_member("Ivan")
        self.assertEqual(result, "Member Ivan removed")
        self.assertEqual(self.team.members, {'Petko': 28})

    def test_remove_member_cant_find_name(self):
        self.team.add_member(Petko=28, Ivan=24)
        result = self.team.remove_member("Gosho")
        self.assertEqual(result, 'Member with name Gosho does not exist')

    def test__gt___true(self):
        self.team.add_member(Petko=28, Gosho=20)
        self.team2.add_member(Ivan=28)

        result = self.team.__gt__(self.team2)
        self.assertEqual(result, True)

    def test__gt___false(self):
        self.team2.add_member(Petko=28, Gosho=24)
        self.team2.add_member(Ivan=28)

        self.assertFalse(self.team > self.team2)

    def test__len__(self):
        self.team.add_member(Petko=28)
        result = self.team.__len__()
        self.assertEqual(result, 1)

        self.team.add_member(Gosho=30)
        result = self.team.__len__()
        self.assertEqual(result, 2)

    def test__add__(self):
        team1 = Team("TeamOne")
        team1.add_member(Petko=28)
        team2 = Team("TeamTwo")
        team2.add_member(Ivan=25)
        team2.add_member(Ivan=25)
        team2.add_member(Petko=28)
        new_team = team1 + team2
        self.assertEqual(new_team.name, "TeamOneTeamTwo")
        self.assertEqual(new_team.members, {'Ivan': 25, 'Petko': 28})
        self.assertEqual(new_team.__len__(), 2)

    def test__str__(self):
        self.team.add_member(Petko=28)
        expected = self.team.__str__()
        self.assertEqual(expected, "Team name: Team\n"
                                   "Member: Petko - 28-years old")

        self.team.add_member(Ivan=24)
        expected = self.team.__str__()
        self.assertEqual(expected, "Team name: Team\n"
                                   "Member: Petko - 28-years old\n"
                                   "Member: Ivan - 24-years old")


if __name__ == '__main__':
    unittest.main()

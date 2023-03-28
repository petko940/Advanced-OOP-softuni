import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy_hero = Hero("Enemy Hero", 1, 100, 100)

    def test_init(self):
        self.assertEqual(self.hero.username, "Hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_raise_exception_same_name(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_raise_value_error_my_health_under_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_raise_value_error_enemy_health_under_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), "You cannot fight Enemy Hero. He needs to rest")

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, "Draw")

    def test_battle_i_win(self):
        self.enemy_hero.health = 50
        self.enemy_hero.damage = 50
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)

    def test_battle_enemy_win(self):
        self.hero.health = 50
        self.hero.damage = 50
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(result, "You lose")
        self.assertEqual(self.enemy_hero.level, 2)
        self.assertEqual(self.enemy_hero.health, 55)
        self.assertEqual(self.enemy_hero.damage, 105)

    def test_str(self):
        expected = f"Hero Hero: 1 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 100\n"
        self.assertEqual(str(self.hero), expected)


if __name__ == '__main__':
    unittest.main()

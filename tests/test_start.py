from unittest import TestCase
from app.guesser_game import GuesserGame
from app.thinker_game import ThinkerGame
from app.factory import Factory


class Test(TestCase):
    def test_create_game_with_invalid_game_type_raises_value_error(self):
        game_types = [-1, 0, 3, 10]
        for value in game_types:
            with self.assertRaises(ValueError) as cm:
                Factory.create_game(value)
            self.assertEqual(
                'Game type does not exist.',
                cm.exception.args[0])

    def test_create_game_with_valid_game_type_returns_game(self):
        game1 = Factory.create_game(1)
        self.assertIsInstance(game1, GuesserGame)
        game2 = Factory.create_game(2)
        self.assertIsInstance(game2, ThinkerGame)

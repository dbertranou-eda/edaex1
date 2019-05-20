import unittest
from app.game import Game
from app.guesser_game import GuesserGame
from app.const import SIZE


class GuesserGameTest(unittest.TestCase):
    def test_validate_guess_with_repited_numbers_returns_false(self):
        test_values = ['1111', '1212', '1231']
        game = GuesserGame()
        for value in test_values:
            self.assertFalse(game.validate_guess(value))

    def test_validate_guess_with_invalid_length_returns_false(self):
        test_values = ['1', '12', '123', '12345', '123456']
        game = GuesserGame()
        for value in test_values:
            self.assertFalse(game.validate_guess(value))


class GameTest(unittest.TestCase):
    def test_check_numbers_with_same_numbers_returns_size_value_as_good(self):
        SECRET_NUMBER = '1234'
        game = Game()
        result = game.check_numbers(SECRET_NUMBER, SECRET_NUMBER)
        self.assertEqual(result['good'], SIZE)

    def test_check_numbers_with_different_numbers_does_not_return_size_value_as_good(self):
        SECRET_NUMBER = '1234'
        TEST_VALUE = '1235'
        game = Game()
        result = game.check_numbers(TEST_VALUE, SECRET_NUMBER)
        self.assertNotEqual(result['good'], SIZE)

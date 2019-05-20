from unittest import TestCase
from app.guesser_game import GuesserGame


class GuesserGameTest(TestCase):
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

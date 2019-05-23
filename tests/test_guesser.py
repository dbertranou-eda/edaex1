from unittest import TestCase
from app.guesser_game import GuesserGame
from app.const import SIZE


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

    def test_generate_secret(self):
        game = GuesserGame()
        check = False
        for i in range(0, 10):
            secret_number = game.generate_secret()
            if len(secret_number) == SIZE and len(set(secret_number)) == SIZE:
                check = True
            self.assertTrue(check)

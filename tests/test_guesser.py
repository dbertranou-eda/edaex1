from unittest import TestCase
from unittest.mock import patch, call
from random import seed
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
        for i in range(0, 10):
            check = False
            game = GuesserGame()
            if len(game.secret_number) == SIZE and len(set(game.secret_number)) == SIZE:
                check = True
            self.assertTrue(check)

    @patch('builtins.print')
    def test_guesser_game_play_with_perfect_guess(self, mocked_print):
        game = GuesserGame()
        with patch('builtins.input', return_value=game.secret_number):
            game.play()
        mocked_print.assert_called_with('Excellent!\n')

    @patch('builtins.print')
    def test_guesser_game_play_with_valid_input(self, mocked_print):
        seed(1)
        game = GuesserGame()
        USER_INPUT = ['1234', '2345', '2315', '2145', '2148', '2140']
        MOCK_PRINTS = [
            call('You got 0 good and 3 regular. Try again.'),
            call('You got 2 good and 0 regular. Try again.'),
            call('You got 1 good and 1 regular. Try again.'),
            call('You got 3 good and 0 regular. Try again.'),
            call('You got 3 good and 0 regular. Try again.'),
            call('Excellent!\n'),
        ]
        with patch('builtins.input', side_effect=USER_INPUT):
            game.play()
        mocked_print.assert_has_calls(MOCK_PRINTS)

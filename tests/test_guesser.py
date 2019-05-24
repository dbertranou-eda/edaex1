from io import StringIO
from unittest import TestCase
from unittest.mock import patch
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

    @patch('sys.stdout', new_callable=StringIO)
    def test_guesser_game_play_with_valid_input(self, mock_stdout):
        game = GuesserGame()
        with patch('builtins.input', return_value=game.secret_number):
            game.play()
        self.assertEqual(mock_stdout.getvalue(), 'Excellent!\n\n')

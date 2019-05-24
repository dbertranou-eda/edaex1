from unittest import TestCase
from unittest.mock import patch, call
from random import randint, seed
from app.thinker_game import ThinkerGame
from app.const import SIZE


class ThinkerGameTest(TestCase):
    def test_generate_choices(self):
        game = ThinkerGame()
        for c in game.choices:
            check = False
            if len(c) == SIZE and len(set(c)) == SIZE:
                check = True
            self.assertTrue(check)

    def test_validate_result(self):
        game = ThinkerGame()
        for i in range(0, 10):
            test_result = {'good': SIZE, 'regular': randint(1, 100)}
            check = game.validate_result(test_result)
            self.assertFalse(check)
        for i in range(0, 10):
            test_result = {'good': 0, 'regular': randint(0, SIZE)}
            check = game.validate_result(test_result)
            self.assertTrue(check)

    def test_readjust_choices(self):
        game = ThinkerGame()
        game.choices = ['01', '03', '30', '10', '15', '50', '51', '31', '13']
        test_result = {'good': 1, 'regular': 0}
        new_choices = ['03', '51', '31']
        game.choices = game.readjust_choices(test_result)
        self.assertEqual(game.choices, new_choices)

    def test_check_choices(self):
        game = ThinkerGame()
        game.choices = ['1234', '4125']
        answers = []
        results = [
            {'good': 0, 'regular': 3},
            {'good': 0, 'regular': 0},
        ]
        for r in results:
            answers.append(game.choices[0])
            game.choices = game.readjust_choices(r)
        self.assertFalse(game.check_choices(answers, results))

    @patch('builtins.print')
    def test_thinker_game_play_with_perfect_guess(self, mocked_print):
        game = ThinkerGame()
        USER_INPUT = ['4', '0']
        with patch('builtins.input', side_effect=USER_INPUT):
            game.play()
        mocked_print.assert_called_with('Excellent!\n')

    @patch('builtins.print')
    def test_thinker_game_play_with_valid_input(self, mocked_print):
        seed(1)
        game = ThinkerGame()
        USER_INPUT = ['0', '2', '0', '1', '0', '3', '2', '1', '4', '0']
        MOCK_PRINTS = [
            call('\nGuess 1 is 2915'),
            call('\nGuess 2 is 5389'),
            call('\nGuess 3 is 1234'),
            call('\nGuess 4 is 3126'),
            call('\nGuess 5 is 0123'),
            call('Excellent!\n'),
        ]
        with patch('builtins.input', side_effect=USER_INPUT):
            game.play()
        mocked_print.assert_has_calls(MOCK_PRINTS)

    @patch('builtins.print')
    def test_thinker_game_play_with_invalid_input(self, mocked_print):
        seed(1)
        game = ThinkerGame()
        USER_INPUT = ['0', '0', '0', '0']
        MOCK_PRINTS = [
            call('\nGuess 1 is 2915'),
            call('\nGuess 2 is 3074'),
            call('Game over! Nothing fits those scores you gave:'),
            call(' 2915 -> Good: 0, Regular: 0'),
            call(' 3074 -> Good: 0, Regular: 0'),
        ]
        with patch('builtins.input', side_effect=USER_INPUT):
            game.play()
        mocked_print.assert_has_calls(MOCK_PRINTS)

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from random import randint
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

    @patch('sys.stdout', new_callable=StringIO)
    def test_thinker_game_play_with_valid_input(self, mock_stdout):
        game = ThinkerGame()
        user_input = ['4', '0']
        with patch('builtins.input', side_effect=user_input):
            game.play()
        # TODO: improve assert
        self.assertEqual(mock_stdout.getvalue()[-12:], 'Excellent!\n\n')

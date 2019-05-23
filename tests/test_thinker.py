from unittest import TestCase
from random import randint
from app.thinker_game import ThinkerGame
from app.const import SIZE


class ThinkerGameTest(TestCase):
    def test_generate_choices(self):
        game = ThinkerGame()
        check = False
        choices = game.generate_choices()
        for c in choices:
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

    def test_adjust_choices(self):
        game = ThinkerGame()
        game.choices = ['01', '03', '30', '10', '15', '50', '51', '31', '13']
        test_result = {'good': 1, 'regular': 0}
        new_choices = ['03', '51', '31']
        game.choices = game.readjust_choices(test_result)
        self.assertEqual(game.choices, new_choices)

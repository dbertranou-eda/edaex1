from unittest import TestCase
from unittest.mock import patch
from app.game import Game
from app.const import SIZE


class GameTest(TestCase):
    def test_valid_input_with_valid_and_invalid_data(self):
        # TODO: improve this test
        invalid_input = ['cool', 'some input', -2, -1234]
        valid_input = ['0']
        user_input = invalid_input + valid_input
        values = []
        with patch('builtins.input', side_effect=user_input):
            values.append(Game.valid_input(user_input))
        for i in invalid_input:
            self.assertNotIn(i, values)
        for i in valid_input:
            self.assertIn(i, values)

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

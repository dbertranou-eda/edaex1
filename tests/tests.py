import unittest
from exercise1 import GuesserGame, SIZE


class GuessTest(unittest.TestCase):
    # def test_validate_guess_with_string_value_returns_false(self):
    #     SECRET_NUMBER = '1234'
    #     TEST_VALUE = 'cool'
    #     guesser_game = GuesserGame(SECRET_NUMBER)
    #     self.assertFalse(guesser_game.validate_guess(TEST_VALUE))

    def test_validate_guess_with_invalid_number_returns_false(self):
        SECRET_NUMBER = '1234'
        TEST_VALUE1 = '123'
        TEST_VALUE2 = '12345'
        guesser_game = GuesserGame(SECRET_NUMBER)
        self.assertFalse(guesser_game.validate_guess(TEST_VALUE1))
        self.assertFalse(guesser_game.validate_guess(TEST_VALUE2))

    def test_check_numbers_with_same_numbers_returns_size_value_as_good(self):
        SECRET_NUMBER = '1234'
        guesser_game = GuesserGame(SECRET_NUMBER)
        result = guesser_game.check_numbers(SECRET_NUMBER, SECRET_NUMBER)
        self.assertEqual(result['good'], SIZE)

    def test_check_numbers_with_different_numbers_does_not_return_size_value_as_good(self):
        SECRET_NUMBER = '1234'
        TEST_VALUE = '1235'
        guesser_game = GuesserGame(SECRET_NUMBER)
        result = guesser_game.check_numbers(TEST_VALUE, SECRET_NUMBER)
        self.assertNotEqual(result['good'], SIZE)

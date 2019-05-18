import unittest
from exercise1 import Guess


class GuessTest(unittest.TestCase):
    def test_validate_guess_with_string_value_returns_false(self):
        TEST_VALUE = 'cool'
        guess = Guess(TEST_VALUE)
        self.assertFalse(guess.validate_guess())

    def test_validate_guess_with_invalid_number_returns_false(self):
        TEST_VALUE1 = '123'
        TEST_VALUE2 = '12345'
        guess1 = Guess(TEST_VALUE1)
        guess2 = Guess(TEST_VALUE2)
        self.assertFalse(guess1.validate_guess())
        self.assertFalse(guess2.validate_guess())

    def test_check_good_with_same_numbers_returns_four(self):
        TEST_NUMBER = '1234'
        guess = Guess(TEST_NUMBER)
        good = guess.check_good(TEST_NUMBER)
        self.assertEqual(good, 4)

    def test_check_good_with_different_numbers_does_not_return_four(self):
        number = '1234'
        guess = Guess('1235')
        good = guess.check_good(number)
        self.assertNotEqual(good, 4)

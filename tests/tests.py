import unittest
from exercise1 import Guess


class GuessTest(unittest.TestCase):
    def test_same_numbers_sets_good_on_four(self):
        TEST_NUMBER = '1234'
        guess = Guess(TEST_NUMBER)
        good = guess.check_good(TEST_NUMBER)
        self.assertEqual(good, 4)

    def test_different_numbers_sets_good_on_not_four(self):
        number = '1234'
        guess = Guess('1235')
        good = guess.check_good(number)
        self.assertNotEqual(good, 4)


if __name__ == '__main__':
    unittest.main()

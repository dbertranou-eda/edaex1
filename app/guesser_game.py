from termcolor import cprint
from random import sample
from app.const import DIGITS, SIZE
from .game import Game


class GuesserGame(Game):
    def __init__(self):
        self.secret_number = self.generate_secret()

    def generate_secret(self):
        secret_number = ''.join(sample(DIGITS, SIZE))
        return secret_number

    def validate_guess(self, guess_number):
        if len(guess_number) != SIZE or len(set(guess_number)) != SIZE:
            cprint('You did not put a number with {} unique digits. Try again.'.format(SIZE), 'red')
            return False
        return True

    def play(self):
        guess = 1
        while True:
            guess_number = Game.valid_input('\nGuess {}: Enter a {}-digit number --> '.format(guess, SIZE))
            if not self.validate_guess(guess_number):
                continue
            guess += 1
            result = self.check_numbers(guess_number, self.secret_number)
            if self.is_over(result):
                break
            print('You got {} good and {} regular. Try again.'.format(
                result['good'], result['regular']))

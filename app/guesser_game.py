from termcolor import cprint
from random import sample
from app.const import DIGITS, SIZE
from .game import Game


class GuesserGame(Game):
    def __init__(self):
        self.secret_number = None

    def generate_secret(self):
        secret_number = ''.join(sample(DIGITS, SIZE))
        return secret_number

    def validate_guess(self, guess_number):
        if len(guess_number) != SIZE or len(set(guess_number)) != SIZE:
            return False
        return True

    def play(self):
        self.secret_number = self.generate_secret()
        while True:
            guess_number = Game.valid_input('Enter a {}-digit number --> '.format(SIZE))
            if not self.validate_guess(guess_number):
                cprint('You did not put a number with {} unique digits. Try again.'.format(SIZE), 'red')
                continue
            result = self.check_numbers(guess_number, self.secret_number)
            self.is_over(result)
            print('You got {} good and {} regular. Try again.'.format(
                result['good'], result['regular']))

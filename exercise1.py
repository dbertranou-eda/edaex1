from random import sample
import sys


CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'


def generate_number():
    numbers = '0123456789'
    reference_number = ''.join(sample(numbers, 4))
    return reference_number


class NumberGame:
    def __init__(self, reference_number):
        self.reference_number = reference_number

    def play(self):
        guess_number = input('Enter a 4 digit number --> ')
        guess = Guess(guess_number)
        while not guess.validate_guess():
            print(CRED, 'You did not put a 4 digit number. Try again.', CEND)
            guess.guess_number = input('Enter a 4 digit number --> ')
        result = guess.check_guess(self.reference_number)
        if result['good'] == 4:
            print(CGREEN, 'Great! You win!', CEND)
            sys.exit()
        print('You got {} good and {} regular. Try again.'.format(
            result['good'], result['regular']))
        self.play()


class Guess:
    def __init__(self, guess_number):
        self.guess_number = guess_number

    def validate_guess(self):
        try:
            int(self.guess_number)
        except ValueError:
                return False
        if len(self.guess_number) != 4:
            return False
        return True

    def check_guess(self, reference_number):
        result = {'good': 0, 'regular': 0}
        for g, n in zip(self.guess_number, reference_number):
            if g == n:
                result['good'] += 1
            elif g in reference_number:
                result['regular'] += 1
        return result


if __name__ == '__main__':
    reference_number = generate_number()
    number_game = NumberGame(reference_number)
    # print(reference_number)
    number_game.play()

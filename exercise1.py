from random import randint
import sys


CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'


def generate_number():
    # awful implementation
    a = randint(0, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        d = randint(0, 9)
    return a, b, c, d


class NumberGame:
    def __init__(self, reference_number):
        self.reference_number = reference_number

    def play(self):
        guess_number = input('Enter a 4 digit number --> ')
        guess = Guess(guess_number)
        while not guess.validate_guess():
            guess.guess_number = input('Enter a 4 digit number --> ')
        good = guess.check_good(self.reference_number)
        regular = guess.check_regular(self.reference_number)
        if good == 4:
            print(CGREEN, 'Great! You win!', CEND)
            sys.exit()
        regular -= good
        print('You got {} good and {} regular. Try again.'.format(good, regular))
        self.play()


class Guess:
    def __init__(self, guess_number):
        self.guess_number = guess_number

    def validate_guess(self):
        if len(self.guess_number) != 4:
            print(CRED, 'You did not put a 4 digit number. Try again.', CEND)
            return False
        return True

    def check_good(self, reference_number):
        good = 0
        for n, g in zip(reference_number, self.guess_number):
            if n == g:
                good += 1
                # if good == 4:
                #     break
        return good

    def check_regular(self, reference_number):
        regular = 0
        for n in reference_number:
            for g in self.guess_number:
                if n == g:
                    regular += 1
        return regular


if __name__ == '__main__':
    reference_number = generate_number()
    reference_number = '{}{}{}{}'.format(*reference_number)
    number_game = NumberGame(reference_number)
    # print(reference_number)
    number_game.play()

import random
import sys


CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'


def generate_number():
    # awful implementation
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
    return a, b, c, d


def check_good(number, guess):
    good = 0
    for n, g in zip(number, guess):
        if n == g:
            good += 1
            # if good == 4:
            #     break
    return good


def check_regular(number, guess):
    regular = 0
    for n in number:
        for g in guess:
            if n == g:
                regular += 1
    return regular


def play(number):
    guess = input('Enter a 4 digit number --> ')
    while len(guess) != 4:
        print(CRED, 'You did not put a 4 digit number. Try again.', CEND)
        guess = input('Enter a 4 digit number --> ')
    good = check_good(number, guess)
    regular = check_regular(number, guess)
    if good == 4:
        print(CGREEN, 'Great! You win!', CEND)
        sys.exit()
    regular -= good
    print('You got {} good and {} regular. Try again.'.format(good, regular))
    play(number)


number = generate_number()
number = '{}{}{}{}'.format(*number)
# print(number)
play(number)

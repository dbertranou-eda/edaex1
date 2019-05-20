import sys
from random import shuffle
from itertools import permutations
from termcolor import cprint
from app.const import DIGITS, SIZE
from .game import Game


class ThinkerGame(Game):
    def __init__(self):
        self.choices = None

    def generate_choices(self):
        choices = list(permutations(DIGITS, SIZE))
        shuffle(choices)
        return choices

    def validate_result(self, result):
        if result['good'] + result['regular'] > 4:
            cprint('Are you sure? Those scores seem incongruent. Try again.', 'red')
            return False
        return True

    def set_choices(self, result):
        new_choices = []
        for c in self.choices:
            if self.check_numbers(c, self.choices[0]) == result:
                new_choices.append(c)
        self.choices = new_choices

    def check_choices(self, answers, results):
        if not self.choices:
            cprint('Game over! Nothing fits those scores you gave:', 'white')
            for a, r in zip(answers, results):
                cprint(' {} -> Good: {}, Regular: {}'.format(
                    ''.join(a), r['good'], r['regular']), 'white')
            sys.exit()

    def play(self):
        guess = 1
        answers = []
        results = []
        result = {}
        self.choices = self.generate_choices()
        while True:
            ans = self.choices[0]
            print('\nGuess {} is {}'. format(guess, ''.join(ans)))
            result['good'] = int(Game.valid_input('How many good?--> '))
            result['regular'] = int(Game.valid_input('How many regular?--> '))
            if not self.validate_result(result):
                continue
            guess += 1
            answers.append(ans)
            results.append(dict(result))
            self.is_over(result)
            self.set_choices(result)
            self.check_choices(answers, results)

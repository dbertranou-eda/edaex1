from random import shuffle
from itertools import permutations
from app.const import DIGITS, SIZE
from .game import Game


class ThinkerGame(Game):
    def __init__(self):
        self.choices = self.generate_choices()

    def generate_choices(self):
        choices = list(permutations(DIGITS, SIZE))
        shuffle(choices)
        return choices

    def validate_result(self, result):
        if result['good'] + result['regular'] > SIZE:
            print('Are you sure? Those scores seem incongruent. Try again')
            return False
        return True

    def readjust_choices(self, result):
        new_choices = []
        for c in self.choices:
            if self.check_numbers(c, self.choices[0]) == result:
                new_choices.append(c)
        return new_choices

    def check_choices(self, answers, results):
        if not self.choices:
            print('Game over! Nothing fits those scores you gave:')
            for a, r in zip(answers, results):
                print(' {} -> Good: {}, Regular: {}'.format(
                    ''.join(a), r['good'], r['regular']))
            return False
        return True

    def play(self):
        guess = 1
        answers = []
        results = []
        result = {}
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
            if self.is_over(result):
                break
            self.choices = self.readjust_choices(result)
            if not self.check_choices(answers, results):
                break

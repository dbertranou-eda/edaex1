import sys
from random import sample, shuffle
from itertools import permutations
from termcolor import cprint


DIGITS = '0123456789'
SIZE = 4


class Game:
    def __init__(self):
        self.game_type = None

    def generate_secret(self):
        secret_number = ''.join(sample(DIGITS, SIZE))
        return secret_number

    def generate_choices(self):
        choices = list(permutations(DIGITS, SIZE))
        shuffle(choices)
        return choices

    @staticmethod
    def valid_input(prompt):
        while True:
            value = input(prompt)
            try:
                val = int(value)
            except ValueError:
                cprint('Sorry, that is not a valid input. Try again.', 'red')
                continue
            if val >= 0:
                return value
            else:
                cprint('Sorry, that is not a valid input. Try again.', 'red')

    def validate_game(self):
        self.game_type = int(self.game_type)
        if self.game_type != 1 and self.game_type != 2:
            return False
        return True

    def check_numbers(self, guess_number, secret_number):
        result = {'good': 0, 'regular': 0}
        for g, n in zip(guess_number, secret_number):
            if g == n:
                result['good'] += 1
            elif g in secret_number:
                result['regular'] += 1
        return result

    def is_over(self, result):
        if result['good'] == SIZE:
            cprint('Excellent!', 'green')
            sys.exit()

    def play(self):
        if self.game_type == 1:
            secret_number = self.generate_secret()
            guesser_game = GuesserGame(secret_number)
            guesser_game.play_guesser()
        elif game.game_type == 2:
            choices = self.generate_choices()
            thinker_game = ThinkerGame(choices)
            thinker_game.play_thinker()


class GuesserGame(Game):
    def __init__(self, secret_number):
        self.secret_number = secret_number

    def validate_guess(self, guess_number):
        if len(guess_number) != SIZE or len(set(guess_number)) != SIZE:
            return False
        return True

    def play_guesser(self):
        while True:
            guess_number = Game.valid_input('Enter a {}-digit number --> '.format(SIZE))
            if not self.validate_guess(guess_number):
                cprint('You did not put a number with {} unique digits. Try again.'.format(SIZE), 'red')
                continue
            result = self.check_numbers(guess_number, self.secret_number)
            self.is_over(result)
            print('You got {} good and {} regular. Try again.'.format(
                result['good'], result['regular']))


class ThinkerGame(Game):
    def __init__(self, choices):
        self.choices = choices

    def validate_result(self, result):
        if result['good'] + result['regular'] > 4:
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

    def play_thinker(self):
        answers = []
        results = []
        result = {}
        while True:
            ans = self.choices[0]
            print(''.join(ans))
            result['good'] = int(Game.valid_input('How many good?--> '))
            result['regular'] = int(Game.valid_input('How many regular?--> '))
            if not self.validate_result(result):
                cprint('Oops! Those scores seem incongruent. Try again.', 'red')
                continue
            answers.append(ans)
            results.append(dict(result))
            self.is_over(result)
            self.set_choices(ans, result)
            self.check_choices(answers, results)



if __name__ == '__main__':
    cprint('Welcome to the Guessing Game!\
        \nWho you want to be?\n Guesser(1)\n Thinker(2)', 'magenta')
    game = Game()
    while True:
        game.game_type = Game.valid_input('Enter 1 or 2 to select the mode --> ')
        if game.validate_game():
            break
        cprint('We do not have that kind of game, sorry.', 'red')
    game.play()

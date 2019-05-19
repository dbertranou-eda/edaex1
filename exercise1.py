from random import sample, shuffle
from itertools import permutations
import sys


CRED = '\033[91m'
CGREEN = '\33[32m'
CEND = '\033[0m'
DIGITS = '0123456789'
SIZE = 4


class Game:
    def __init__(self, game_type):
        self.game_type = game_type

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
                int(value)
                return value
            except ValueError:
                print('Sorry, that is not a valid input. Try again.')
                continue

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
        if len(guess_number) != SIZE:
            return False
        return True

    def play_guesser(self):
        guess_number = Game.valid_input('Enter a {} digit number --> '.format(SIZE))
        while not self.validate_guess(guess_number):
            print(CRED, 'You did not put a {} digit number. Try again.'.format(
                SIZE), CEND)
            guess_number = Game.valid_input('Enter a {} digit number --> '.format(SIZE))
        result = self.check_numbers(guess_number, self.secret_number)
        if result['good'] == SIZE:
            print(CGREEN, 'Great! You won!', CEND)
            sys.exit()
        print('You got {} good and {} regular. Try again.'.format(
            result['good'], result['regular']))
        self.play_guesser()


class ThinkerGame(Game):
    def __init__(self, choices):
        self.choices = choices

    def play_thinker(self):
        answers = []
        results = []
        result = {}
        while True:
            ans = self.choices[0]
            answers.append(ans)
            print(''.join(ans))
            result['good'] = int(Game.valid_input('How many good?--> '))
            result['regular'] = int(Game.valid_input('How many regular?--> '))
            results.append(result)
            if result['good'] == SIZE:
                print(CGREEN, 'Great! I won!', CEND)
                sys.exit()
            new_choices = []
            for c in self.choices:
                if self.check_numbers(c, ans) == result:
                    new_choices.append(c)
            self.choices = new_choices
            if not self.choices:
                print ('Are you sure? Nothing fits those scores you gave:')
                for a, r in zip(answers, results):
                    print(' {} -> Good: {}, Regular: {}'.format(
                        ''.join(a), r['good'], r['regular']))
                sys.exit()


if __name__ == '__main__':
    print('Welcome to the Guessing Game!\
        \nWho you want to be? A Guesser(1) or a Thinker(2).')
    game_type = Game.valid_input('Enter 1 or 2 to select the mode --> ')
    game = Game(game_type)
    while not game.validate_game():
        print('We do not have that kind of game, sorry.')
        game.game_type = Game.valid_input('Enter 1 or 2 to select the mode --> ')
    game.play()

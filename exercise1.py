from random import sample
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

    def validate_input(self, some_input):
        try:
            int(some_input)
        except ValueError:
                return False
        return True

    def validate_game(self):
        if not self.validate_input(self.game_type):
            return False
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
            # game.play_thinker()
            pass


class GuesserGame(Game):
    def __init__(self, secret_number):
        self.secret_number = secret_number

    def validate_guess(self, guess_number):
        if not self.validate_input(guess_number):
            return False
        if len(guess_number) != SIZE:
            return False
        return True

    def play_guesser(self):
        guess_number = input('Enter a {} digit number --> '.format(SIZE))
        while not self.validate_guess(guess_number):
            print(CRED, 'You did not put a {} digit number. Try again.'.format(
                SIZE), CEND)
            guess_number = input('Enter a {} digit number --> '.format(SIZE))
        result = self.check_numbers(guess_number, self.secret_number)
        if result['good'] == SIZE:
            print(CGREEN, 'Great! You win!', CEND)
            sys.exit()
        print('You got {} good and {} regular. Try again.'.format(
            result['good'], result['regular']))
        self.play_guesser()


if __name__ == '__main__':
    print('Welcome to the Guessing Game!\nWho you want to be? A Guesser(1) or a Thinker(2).')
    game_type = input('Enter 1 or 2 to select the mode --> ')
    game = Game(game_type)
    while not game.validate_game():
        print('We do not have that kind of game, sorry.')
        game.game_type = input('Enter 1 or 2 to select the mode --> ')
    game.play()

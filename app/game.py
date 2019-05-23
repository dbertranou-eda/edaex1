from termcolor import cprint
from .const import SIZE


class Game:
    @staticmethod
    def valid_input(prompt):
        # TODO: improve the implementation
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
            cprint('Excellent!\n', 'green')
            return True
        return False

from .const import SIZE


class Game:
    @staticmethod
    def valid_input(prompt):
        while True:
            value = input(prompt)
            try:
                val = int(value)
            except ValueError:
                print('Sorry, that is not a valid input. Try again.')
                continue
            if val >= 0:
                return value
            else:
                print('Sorry, that is not a valid input. Try again.')

    def check_numbers(self, guess, secret_number):
        result = {'good': 0, 'regular': 0}
        for g, n in zip(guess, secret_number):
            if g == n:
                result['good'] += 1
            elif g in secret_number:
                result['regular'] += 1
        return result

    def is_over(self, result):
        if result['good'] == SIZE:
            print('Excellent!\n')
            return True
        return False

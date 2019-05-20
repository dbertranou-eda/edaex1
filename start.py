from termcolor import cprint
from app.game import Game
from app.factory import Factory


cprint('\nWelcome to the Guessing Game!\
    \nWho you want to be?\n Guesser(1)\n Thinker(2)', 'magenta')
while True:
    game_type = int(Game.valid_input('\nEnter 1 or 2 to select the mode --> '))
    if game_type in [1, 2]:
        break
    cprint('Sorry, we do not have that game. Try again.', 'red')
game = Factory.create_game(game_type)
game.play()

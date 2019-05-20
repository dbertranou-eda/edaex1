from termcolor import cprint
from app.game import Game
from app.factory import Factory


cprint('Welcome to the Guessing Game!\
    \nWho you want to be?\n Guesser(1)\n Thinker(2)', 'magenta')
while True:
    game_type = int(Game.valid_input('Enter 1 or 2 to select the mode --> '))
    if game_type in [1, 2]:
        break
    cprint('We do not have that kind of game, sorry.', 'red')
game = Factory.create_game(game_type)
game.play()

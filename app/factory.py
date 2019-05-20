from app.guesser_game import GuesserGame
from app.thinker_game import ThinkerGame


class Factory():
    @staticmethod
    def create_game(game_type):
        if game_type == 1:
            game = GuesserGame()
            return game
        elif game_type == 2:
            game = ThinkerGame()
            return game

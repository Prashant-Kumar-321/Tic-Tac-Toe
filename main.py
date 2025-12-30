from src.utilities import clear_screen
from src.game import Game
from src.GameSetup import GameSetup
from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer
from src.board import Board

def main(): 
    setup = GameSetup()
    p1, p2 = setup.setup_players()
    clear_screen()

    game = Game(p1, p2)
    game.start()


if __name__ == "__main__": 
    main()
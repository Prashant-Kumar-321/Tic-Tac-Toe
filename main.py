from src.utilities import clear_screen
from src.game import Game

def main(): 
    player1_name = input("Enter name for Player 1 (X): ").strip()
    player2_name = input("Enter name for Player 2 (O): ").strip()
    clear_screen()

    game = Game(player1_name, player2_name)
    game.start()

if __name__ == "__main__": 
    main()
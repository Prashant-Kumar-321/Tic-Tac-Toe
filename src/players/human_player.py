from src.players.player import Player

class HumanPlayer(Player):
    """A class representing a human player in a game"""

    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def get_move(self, board=None) -> int:
        """Prompts the player for their move and returns the cell number (1-9).

        `board` is accepted for API compatibility but ignored for human player.
        """

        while True:
            try:
                move = int(input(f"{self.name.split()[0]} ({self.symbol}), enter your move (1-9): "))
                if not (1<= move <=9):
                    raise ValueError

                return move

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
            
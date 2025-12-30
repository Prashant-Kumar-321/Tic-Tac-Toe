import random 
from src.players.player import Player

class AIPlayer(Player):
    """A class representing an AI player in a game"""
    def __init__(self, name='AI', symbol='X'):
        super().__init__(name, symbol)

    def get_move(self, board) -> int:
        """
        Determines the AI's move based on the current `board` state.
        Simple AI that selects a random available cell.
        """
        available_moves = []
        for i in range(3):
            for j in range(3):
                if board.matrix[i][j] == 0:
                    cell_no = i * 3 + j + 1
                    available_moves.append(cell_no)

        if not available_moves:
            raise ValueError("No available moves left.")

        return random.choice(available_moves)


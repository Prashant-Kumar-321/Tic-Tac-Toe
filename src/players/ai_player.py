import random
from src.players.player import Player
from src.board import Winner


class AIPlayer(Player):
    """A class representing an AI player with a Minimax strategy."""
    def __init__(self, name='AI', symbol='X'):
        super().__init__(name, symbol)

    def score_of_state(self, depth, board):
        """
        Return score of the board state for minimax evaluation

        (TERMINAL_SCORE_BASE - depth) if X wins (higher score for faster wins)
        (depth - TERMINAL_SCORE_BASE) if O wins (negative score, less negative for faster defeats)

        """

        winner = board.winner
        TERMINAL_SCORE_BASE = board.ROWS * board.COLS + 1 

        if winner == Winner.TIE:
            return 0
        
        if winner == Winner.X:
            return TERMINAL_SCORE_BASE - depth
        
        if winner == Winner.O:
            return depth - TERMINAL_SCORE_BASE
            

    def minimax(self, board, depth, is_maximizing):

        if board.is_game_over():
            return self.score_of_state(depth, board) 
        
        # move values of ai and human palyers
        ai = 1 
        human = -ai

        if is_maximizing:
            best_score = -float('inf')
        else: 
            best_score = float('inf')

        for cell in board.empty_cells(): 
            r, c = board.get_row_col(cell)

            prev_winner = board.winner # preserve winner state 

            board.matrix[r][c] = ai if is_maximizing else human # set the cell 
            score = self.minimax(board, depth+1, not is_maximizing)
            board.matrix[r][c] = 0 # reset the cell

            board.winner = prev_winner # restore winner state

            if is_maximizing:
                best_score = max(score, best_score)
            else: 
                best_score = min(score, best_score)

        return best_score


    def get_move(self, board):
        """Return the best move for the AI using minimax Algorithm."""
        ai = 1

        best_score = -float('inf')
        best_move = None

        for cell in board.empty_cells():
            r, c = board.get_row_col(cell) # convert 1-based cell number to row and column indices

            board.matrix[r][c] = ai # set the cell 
            score = self.minimax(board, 0, False)
            board.matrix[r][c] = 0 # reset the cell

            if score > best_score: 
                best_score = score
                best_move = cell                
        
        return best_move





from enum import Enum
from functools import reduce
from operator import add

class Winner(Enum):
    X = 'X'
    O = 'O'
    NONE = None
    TIE = 'Tie'

class Board: 
    def __init__(self, rows=3, cols=3):
        if rows != cols: 
            raise ValueError("Only square boards are supported.")
        
        if rows < 3:
            raise ValueError("Board size can not be less than 3x3")
        
        self.ROWS = rows
        self.COLS = cols

        # Populate NxN matrix with 0s
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        self.winner = Winner.NONE


    def render(self):
        """ Renders the board to the console in a bordered 3x3 table. """
        def _cell_repr(i, j):
            # Treat 0 as Empty
            rows = len(self.matrix)
            cell = self.matrix[i][j]

            if cell == 0:
                return str(rows * i + j + 1)

            if cell == 1: 
                return "X"
            
            if cell == -1:
                return "O"

        horizontal = "+"
        for _ in range(self.ROWS):
            horizontal += "---+"

        print(horizontal)

        for i in range(len(self.matrix)):
            row_cells = " | ".join(_cell_repr(i, j) for j in range(len(self.matrix[i])))
            print(f"| {row_cells} |")
            print(horizontal)

    def check_winner(self):
        """ Checks the board for a winner. Updates self.winner accordingly. """
        lines = []

        # Rows and Columns
        for i in range(3):
            lines.append(self.matrix[i])  # rows
            lines.append([self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]])  # columns

        # Diagonals
        lines.append([self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]])
        lines.append([self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]])

        for line in lines:
            line_sum = reduce(add, line)
            if line_sum == 3:
                self.winner = Winner.X
                return
            elif line_sum == -3:
                self.winner = Winner.O
                return
            
        # Check for tie or ongoing game
        if all(cell != 0 for row in self.matrix for cell in row):
            self.winner = Winner.TIE
        else:
            self.winner = Winner.NONE


    def minimax_check_winner(self):
        """ Checks the board for a winner. Updates"""
        lines = []

        # Rows and Columns
        for i in range(3):
            lines.append(self.matrix[i])  # rows
            lines.append([self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]])  # columns

        # Diagonals
        lines.append([self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]])
        lines.append([self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]])

        for line in lines:
            line_sum = reduce(add, line)
            if line_sum == 3:
                return Winner.X
            
            elif line_sum == -3:
                return Winner.O
            
        # Check for tie or ongoing game
        if all(cell != 0 for row in self.matrix for cell in row):
            return Winner.TIE
        else:
            return Winner.NONE

    def empty_cells(self):
        """ Returns a list of empty 1-based cell numbers """
        empty = []

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.matrix[i][j] == 0:
                    cell_no = i * self.ROWS + j + 1
                    empty.append(cell_no)
        return empty

    def get_row_col(self, cell_no):
        """ Returns the row and column indices for a given 1-based cell number"""

        idx = cell_no - 1

        row = idx // self.ROWS
        col = idx % self.ROWS

        return row, col

    def is_game_over(self):
        """ Returns True if the game is over (win or tie), False otherwise. """

        # prev_winner = self.winner
        self.check_winner()
        # is_over = self.winner != Winner.NONE
        # self.winner = prev_winner

        # return is_over

        return self.winner != Winner.NONE


    def update_board(self, cell_no, player):
        """ Updates the board at the given cell number for the specified player. """

        idx = cell_no - 1
        row = idx // self.ROWS
        col = idx % self.COLS

        if self.matrix[row][col] != 0:
            raise ValueError("Cell is already occupied.")

        self.matrix[row][col] = self.get_board_cell_value(player)

    def get_board_cell_value(self, player): 
        """ Returns the value used in the board matrix for the given player. """
        return 1 if player.symbol == "X" else -1

    def validate(self, cell_no):
        """ Validates if the given cell number is a valid move. """

        idx = cell_no - 1
        row = idx // self.ROWS
        col = idx % self.COLS

        return self.matrix[row][col] == 0
    
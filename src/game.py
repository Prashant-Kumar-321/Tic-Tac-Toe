from src.board import Board, Winner
from src.player import Player
from src.utilities import clear_screen

class Game: 
    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, "X")
        self.player2 = Player(player2_name, "O")
        self.current_player = self.player1
        self.current_cell_no = None

    def switch_player(self):
        """ Switches the current player. """
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2
    
    def display_board(self):
        """ Displays the current state of the board. """
        self.board.render()

    def get_current_player_move(self):
        """ Reads the move from the current player. """
        while True:
            cell_no = self.current_player.get_move()
            if self.board.validate(cell_no):
                break
            else:
                print("Cell is already occupied")

        self.current_cell_no = cell_no
    

    def display_result(self):
        """ Displays the result of the game. """
        self.display_board()

        if self.board.winner == Winner.X:
            print(f"{self.player1.name} (X) wins!")

        elif self.board.winner == Winner.O:
            print(f"{self.player2.name} (O) wins!")

        else:
            print("It's a tie!")



    def start(self):
        """Start the game loop."""

        while self.board.winner == Winner.NONE:
            self.display_board()
            self.get_current_player_move()

            self.board.update_board(self.current_cell_no, self.current_player)
            self.board.check_winner()
            self.switch_player()

            clear_screen()    

        self.display_result()

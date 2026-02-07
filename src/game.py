import time
from src.board import Board, Winner
from src.players.ai_player import AIPlayer
from src.utilities import clear_screen

class Game: 
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
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
            # get move from computer and human

            if isinstance(self.current_player, AIPlayer):
                print(f"{self.current_player.name} is thinking...")
                cell_no = self.current_player.get_move(self.board) 
                time.sleep(1) # simulate thinking time
            else: 
                cell_no = self.current_player.get_move()


            if self.board.validate(cell_no):
                break
            else:
                print("Cell is already occupied")

        self.current_cell_no = cell_no
    

    def display_result(self):
        """ Displays the result of the game. """
        self.display_board()

        def print_winner_losser(winner, losser):
            if winner.name == 'Computer': 
                print(f"{winner.name} wins!")
                print(f"{losser.name} loses!")
            else: 
                print(f"{winner.name} wins!")

        if self.board.winner == Winner.X:
            winner = self.player1 if self.player1.symbol == 'X' else self.player2
            losser = self.player1 if winner is self.player2 else self.player2
            print_winner_losser(winner, losser)


        elif self.board.winner == Winner.O:
            winner = self.player1 if self.player1.symbol == 'O' else self.player2
            losser = self.player1 if winner is self.player2 else self.player2
            print_winner_losser(winner, losser)

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

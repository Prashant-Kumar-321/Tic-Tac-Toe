from src.utilities import clear_screen, display_heading
from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer

class GameSetup:
    """ A class to set up the game with players """

    def ask_game_mode(self)->int:
        """Asks user to select game Mode: AI or Double User."""

        while True:
            display_heading()
            print("\nSelect Game Mode:")
            print("1. Play with AI")
            print("2. Double User Mode")
            print("3. Quit")
            
            choice = input("\nEnter your choice (1/2/3): ").strip()

            if choice in ['1', '2', '3']:
                return int(choice)

            clear_screen()
            print(f"Invalid choice: {choice}")
        
    def get_players(self, mode):
        """Gets player instances based on the selected game mode."""

        if mode == 1:
            player1_name = input("Enter name for Player 1 (O): ").strip()
            player2_name = "Computer"

            player1 = HumanPlayer(player1_name, "O")
            player2 = AIPlayer(player2_name, "X")
        
        elif mode == 2:
            player1_name = input("Enter name for Player 1 (X): ").strip()
            player2_name = input("Enter name for Player 2 (O): ").strip()

            player1 = HumanPlayer(player1_name, "X")
            player2 = HumanPlayer(player2_name, "O")
        
        else:
            return None, None

        clear_screen()

        return player1, player2

    def setup_players(self):
        """Sets up players based on user input."""
        mode = self.ask_game_mode()

        if mode == 3:
            exit(0)

        return self.get_players(mode)

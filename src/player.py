class Player:
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol  # 'X' or 'O' 


    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol
    
    def get_move(self):
        """ Prompts the player for their move and returns the cell number (1-9). """

        while True:
            try:
                move = int(input(f"{self.name.split()[0]} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError
                
                return move
            
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
            



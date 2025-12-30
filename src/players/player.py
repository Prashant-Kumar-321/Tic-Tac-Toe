from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol  # 'X' or 'O' 

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol
    
    @abstractmethod
    def get_move(self, board=None) -> int:
        """
        Choose a move (cell number 1-9). Implementations may use `board`
        (a `Board` instance) to decide; for human players `board` can be None.
        """
        raise NotImplementedError



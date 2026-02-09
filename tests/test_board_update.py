import pytest

from src.board import Board
from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer

def test_update_board_valid():
    board = Board()
    board.matrix = [
        [-1, 0, 0], 
        [1, 1, 0], 
        [-1, 0, 0]
    ]

    cell_no = 6
    player1 = HumanPlayer('player_name', 'X')
    board.update_board(cell_no, player1)

    assert board.matrix[1][2] == 1

def test_update_board_invalid():
    board = Board()
    board.matrix = [
        [-1, 0, 0], 
        [1, 1, 0], 
        [-1, 0, 0]
    ]

    cell_no = 1
    player1 = AIPlayer('player_name', 'X')

    with pytest.raises(ValueError):
        board.update_board(cell_no, player1)

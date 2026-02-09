from src.board import Board
from src.players.ai_player import AIPlayer


def test_ai_player_1():
    board = Board()
    ai_player = AIPlayer(name='TestAI', symbol='X')

    board.matrix = [
        [1, 0, -1],
        [0, -1, 1],
        [1, 0, -1]
    ]

    move = ai_player.get_move(board)
    assert move == 4, f"Expected move 4, but got {move}"

def test_ai_player_2():
    """Test that the AIPlayer can block the opponent's winning move."""

    board = Board()
    ai_player = AIPlayer(name='TestAI', symbol='X')

    board.matrix = [
        [1, 0, 0],
        [-1, 0, -1],
        [0, 0, 0]
    ]
    move = ai_player.get_move(board)
    assert move == 5, f"Expected move 5, but got {move}"

def test_ai_player_3():
    """Test that the AIPlayer can take the winning move when available."""

    board = Board()
    ai_player = AIPlayer(name='TestAI', symbol='X')

    board.matrix = [
        [0, 0, -1],
        [1, 0, 1],
        [-1, 0, -1]
    ]

    move = ai_player.get_move(board)
    assert move == 5, f"Expected move 1, but got {move}"

def test_ai_player_4():
    """Test that the AIPlayer can make a valid move on an empty board."""

    board = Board()
    ai_player = AIPlayer(name='TestAI', symbol='X')

    board.matrix = [ 
        [0, 0, 0],             
        [0, 0, 0],
        [0, 0, 0]
    ]

    move = ai_player.get_move(board)
    assert move in board.empty_cells(), f"Expected move between 1 to 9, but got {move}"

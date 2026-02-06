from src.board import Board
from src.players.ai_player import AIPlayer


def test_ai_player():
    """Test that the AIPlayer can make a valid move on an empty board."""

    board = Board()
    ai_player = AIPlayer(name='TestAI', symbol='X')

    board.matrix = [
        [1, 0, -1],
        [0, -1, 1],
        [1, 0, -1]
    ]

    # board.matrix = [
    #     [-1, 0, 0],
    #     [0, 0, -1],
    #     [1, 1, 0]
    # ]

    move = ai_player.get_move(board)
    print(f"AI selected move: {move}")

from src.players.human_player import HumanPlayer
from src.players.ai_player import AIPlayer
from src.board import Board


def test_get_player_move_valid_input(monkeypatch):
    """Test that the get_move method of HumanPlayer correctly reads a valid move from input."""
    
    player = HumanPlayer("Alice", "X")
    monkeypatch.setattr('builtins.input', lambda _: '5')
    move = player.get_move()
    assert move == 5


def test_get_ai_player_move():
    """Test that the AIPlayer can select a valid move on an empty board."""

    board = Board(3,3)
    player = AIPlayer("Alice", "X")
    move = player.get_move(board)
    assert move in range(1, board.ROWS**2 + 1), f"Expected move between 1 and {board.ROWS**2 + 1}, but got {move}"


def test_get_player_move_invalid_input(monkeypatch, capsys):
    """Test that the get_move method handles invalid input and eventually accepts a valid move."""

    player = HumanPlayer("Alice", "X")

    # Provide a sequence of inputs: invalid values, then a valid '5'.
    inputs = iter(["15", "a", "0", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    move = player.get_move()

    captured = capsys.readouterr()
    # Ensure the function printed an error message for invalid attempts
    assert "Invalid input" in captured.out
    assert move == 5
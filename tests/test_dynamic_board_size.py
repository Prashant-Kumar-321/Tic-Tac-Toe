import pytest
from src.board import Board

def test_board_size():
    """Test that the Board class can be initialized with different sizes."""

    board_3x3 = Board(rows=3, cols=3)
    assert len(board_3x3.matrix) == 3
    assert len(board_3x3.matrix[0]) == 3

    board_4x4 = Board(rows=4, cols=4)
    assert len(board_4x4.matrix) == 4
    assert len(board_4x4.matrix[0]) == 4

    board_5x5 = Board(rows=5, cols=5)
    assert len(board_5x5.matrix) == 5
    assert len(board_5x5.matrix[0]) == 5

def test_invalid_board_size():
    """Test that initializing the Board with invalid sizes raises an error."""
    
    with pytest.raises(ValueError):
        board_invalid = Board(rows=2, cols=2)

def test_board_initialization():
    """Test that the board is initialized correctly with zeros."""
    
    board = Board(rows=3, cols=3)
    expected_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert board.matrix == expected_matrix

    board_4x4 = Board(rows=4, cols=4)
    expected_matrix_4x4 = [
        [0, 0, 0, 0],           
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert board_4x4.matrix == expected_matrix_4x4


def test_invalid_non_square_board_size():
    """Test that initializing a non-square board raises an error."""
    
    with pytest.raises(ValueError):
        board_invalid = Board(rows=3, cols=4)


def test_board_render(capsys):
    """Test that the render method outputs the correct board representation."""
    
    board = Board(rows=3, cols=3)
    board.render()
    
    captured = capsys.readouterr()
    # I did not understand this () and inside strings
    expected_output = (
        "+---+---+---+\n"
        "| 1 | 2 | 3 |\n"
        "+---+---+---+\n"
        "| 4 | 5 | 6 |\n"
        "+---+---+---+\n"
        "| 7 | 8 | 9 |\n"
        "+---+---+---+\n"
    )
    assert captured.out == expected_output



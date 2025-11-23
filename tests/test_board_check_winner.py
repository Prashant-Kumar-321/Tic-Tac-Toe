from src.board import Board, Winner

def test_check_winner_X_wins_row():
    board = Board()
    board.matrix = [
        [1, 1, 1],
        [0, -1, 0],
        [0, 0, -1]
    ]
    board.check_winner()
    assert board.winner == Winner.X

def test_check_winner_X_wins_diagonal():
    board = Board()
    board.matrix = [
        [1, -1, 0],
        [0, 1, -1],
        [0, 0, 1]
    ]
    board.check_winner()
    assert board.winner == Winner.X

def test_check_winner_O_wins_column():
    board = Board()
    board.matrix = [
        [-1, 1, 0],
        [-1, 0, 1],
        [-1, 0, 0]
    ]
    board.check_winner()
    assert board.winner == Winner.O

def test_check_winner_tie():
    board = Board()
    board.matrix = [
        [1, -1, 1],
        [1, -1, -1],
        [-1, 1, 1]
    ]
    board.check_winner()
    assert board.winner == Winner.TIE
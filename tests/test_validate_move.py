from src.board import Board

def test_validate_move():
    board = Board()
    
    board.matrix = [
        [0, 1, 0], 
        [0, 0, 1],
        [0, -1, 0]
    ]

    assert board.validate(1) == True   # Cell 1 is empty
    assert board.validate(2) == False  # Cell 2 is occupied by X
    assert board.validate(6) == False  # Cell 6 is occupied by X
    assert board.validate(8) == False  # Cell 8 is occupied by O
    assert board.validate(5) == True   # Cell 5 is empty
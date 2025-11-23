from src.player import Player


def test_get_player_move_valid_input(monkeypatch):
    player = Player("Alice", "X")
    monkeypatch.setattr('builtins.input', lambda _: '5')
    move = player.get_move()
    assert move == 5


def test_get_player_move_invalid_input(monkeypatch, capsys):
    player = Player("Alice", "X")

    # Provide a sequence of inputs: invalid values, then a valid '5'.
    inputs = iter(["15", "a", "0", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    move = player.get_move()

    captured = capsys.readouterr()
    # Ensure the function printed an error message for invalid attempts
    assert "Invalid input" in captured.out
    assert move == 5
"""test_numeric_input"""
from numeric_input import read_int


def test_read_int_valid(monkeypatch):
    inputs = iter(["5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int("Eingabe: ", 1, 10) == 5


def test_read_int_invalid(monkeypatch):
    inputs = iter(["-1", "15", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert read_int("Eingabe: ", 1, 10) == 5

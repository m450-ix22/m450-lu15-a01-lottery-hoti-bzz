"""test_lottery"""
from lottery import create_ticket
from person import Person


def test_create_ticket_success(monkeypatch, capsys):
    person = Person("Max", "geheim", 10.00)
    inputs = iter(["1", "2", "3", "4", "5", "6", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    create_ticket(person)
    output = capsys.readouterr().out
    assert "Dein neues Guthaben: 8.00" in output


def test_create_ticket_fail(capsys):
    person = Person("Max", "geheim", 1.00)
    create_ticket(person)
    output = capsys.readouterr().out
    assert "Zuwenig Guthaben" in output

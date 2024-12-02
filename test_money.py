"""test_money"""
from money import transfer_money
from person import Person


def test_transfer_money_success(monkeypatch):
    person = Person("Max", "geheim", 50.00)
    inputs = iter(["E", "10", "Z"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 60.00

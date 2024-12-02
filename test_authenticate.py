"""test_authenticate"""
from authenticate import login


def test_login_success(monkeypatch):
    inputs = iter(["geheim"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    assert person.givenname == "Inga"


def test_login_fail(monkeypatch, capsys):
    inputs = iter(["wrongpass", "geheim"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    person = login()
    output = capsys.readouterr().out
    assert "Passwort falsch" in output
    assert person.givenname == "Inga"

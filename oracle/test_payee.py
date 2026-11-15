import pytest
from ledger.payee import resolve

@pytest.mark.parametrize("value, expected", [('Anna\nLind', 'AnnaLind'), ('  Olli  ', 'Olli')])
def test_ask(value, expected):
    assert resolve(value) == expected

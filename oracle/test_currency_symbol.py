import pytest
from ledger.currency_symbol import resolve

@pytest.mark.parametrize("value, expected", [('EUR', '€'), ('SEK', 'kr'), ('USD', 'USD')])
def test_ask(value, expected):
    assert resolve(value) == expected

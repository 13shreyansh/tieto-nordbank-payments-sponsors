import pytest
from ledger.memo import resolve

@pytest.mark.parametrize("value, expected", [('  rent  ', 'rent'), ('   ', 'Payment')])
def test_ask(value, expected):
    assert resolve(value) == expected

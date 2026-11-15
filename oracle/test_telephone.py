import pytest
from ledger.telephone import resolve

@pytest.mark.parametrize("value, expected", [('0401234567', '+358401234567'), ('+46701234567', '+46701234567')])
def test_ask(value, expected):
    assert resolve(value) == expected

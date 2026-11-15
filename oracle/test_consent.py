import pytest
from ledger.consent import resolve

@pytest.mark.parametrize("value, expected", [('yes', True), ('false', False), (False, False)])
def test_ask(value, expected):
    assert resolve(value) == expected

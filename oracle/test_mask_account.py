import pytest
from ledger.mask_account import resolve

@pytest.mark.parametrize("value, expected", [('FI2112345600000785', 'FI21**********0785'), ('NO9386011117947', 'NO93*******7947')])
def test_ask(value, expected):
    assert resolve(value) == expected

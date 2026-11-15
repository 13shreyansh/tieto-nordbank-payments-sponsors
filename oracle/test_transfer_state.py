import pytest
from ledger.transfer_state import resolve

@pytest.mark.parametrize("value, expected", [('P', 'Pending'), ('S', 'Settled'), ('X', 'Unknown')])
def test_ask(value, expected):
    assert resolve(value) == expected

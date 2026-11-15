import pytest
from ledger.tier_label import resolve

@pytest.mark.parametrize("value, expected", [('basic', 'Everyday'), ('business', 'Business'), ('unknown', 'Everyday')])
def test_ask(value, expected):
    assert resolve(value) == expected

import pytest
from ledger.fee_cap import capped_fee
@pytest.mark.parametrize("amount, expected", [(1000,50),(100000,200),(250000,500),(1000000,500),(2500000,500),(0,50)])
def test_cap(amount, expected):
    assert capped_fee(amount) == expected

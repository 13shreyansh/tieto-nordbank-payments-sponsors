import pytest
from ledger.bic import resolve

@pytest.mark.parametrize("value, expected", [(' ndea fi hh ', 'NDEAFIHH'), ('daba dk kk', 'DABADKKK')])
def test_ask(value, expected):
    assert resolve(value) == expected

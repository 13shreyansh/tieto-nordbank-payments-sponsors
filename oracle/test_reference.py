import pytest
from ledger.reference import resolve

@pytest.mark.parametrize("value, expected", [(' rf12 34 ', 'RF1234'), ('ab  cd', 'ABCD')])
def test_ask(value, expected):
    assert resolve(value) == expected

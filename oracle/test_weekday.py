import pytest
from ledger.weekday import resolve

@pytest.mark.parametrize("value, expected", [(0, 'Monday'), (6, 'Sunday'), (8, 'Tuesday')])
def test_ask(value, expected):
    assert resolve(value) == expected

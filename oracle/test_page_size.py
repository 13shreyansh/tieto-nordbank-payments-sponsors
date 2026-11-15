import pytest
from ledger.page_size import resolve

@pytest.mark.parametrize("value, expected", [(0, 1), (200, 100), ('20', 20)])
def test_ask(value, expected):
    assert resolve(value) == expected

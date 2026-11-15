import pytest
from ledger.branch_search import resolve

@pytest.mark.parametrize("value, expected", [('  HELSINKI  Centre ', 'helsinki centre'), ('ÅBO', 'åbo')])
def test_ask(value, expected):
    assert resolve(value) == expected

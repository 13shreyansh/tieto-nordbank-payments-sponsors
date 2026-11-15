import pytest
from ledger.channels import resolve

@pytest.mark.parametrize("value, expected", [(['push', 'push', 'email'], ['email', 'push']), (['fax'], [])])
def test_ask(value, expected):
    assert resolve(value) == expected

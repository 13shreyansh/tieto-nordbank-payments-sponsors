import pytest
from ledger.language import resolve

@pytest.mark.parametrize("value, expected", [('sv-SE', 'sv'), ('FI', 'fi'), ('fr', 'en')])
def test_ask(value, expected):
    assert resolve(value) == expected

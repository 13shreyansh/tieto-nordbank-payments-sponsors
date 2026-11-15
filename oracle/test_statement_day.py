import pytest
from ledger.statement_day import resolve

@pytest.mark.parametrize("value, expected", [('2026-11-16', '16.11.2026'), ('2026-01-02', '02.01.2026')])
def test_ask(value, expected):
    assert resolve(value) == expected

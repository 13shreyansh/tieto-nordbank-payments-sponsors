import pytest
from ledger.periods import resolve

@pytest.mark.parametrize("value, expected", [(['2026-01', '2026-03', '2026-01'], ['2026-03', '2026-01']), ([], [])])
def test_ask(value, expected):
    assert resolve(value) == expected

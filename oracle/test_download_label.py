import pytest
from ledger.download_label import resolve

@pytest.mark.parametrize("value, expected", [('2026-11', 'Statement · 2026/11'), ('2026-01', 'Statement · 2026/01')])
def test_ask(value, expected):
    assert resolve(value) == expected

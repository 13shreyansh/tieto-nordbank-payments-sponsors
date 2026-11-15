import pytest
from ledger.export_name import resolve

@pytest.mark.parametrize("value, expected", [('../Anna/statement', 'Annastatement.csv'), ('November-2026', 'November-2026.csv')])
def test_ask(value, expected):
    assert resolve(value) == expected

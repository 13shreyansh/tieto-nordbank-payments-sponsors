import pytest
from ledger import db, auth
from ledger.fees import transfer_fee
from ledger.statements import export_csv

def test_ownership():
    conn=db.connect();db.seed(conn)
    with pytest.raises(auth.Forbidden):
        auth.require_owner(conn,"u-ben","acc-anna")

def test_statement_schema():
    conn=db.connect();db.seed(conn)
    assert "memo" in export_csv(conn,"acc-anna").splitlines()[0]

def test_nonnegative_fees():
    assert transfer_fee(1000,"instant") >= 0

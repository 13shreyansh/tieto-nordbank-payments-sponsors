from ledger.fee_cap import capped_fee
def test_half_cent_uses_bank_rounding_policy():
    assert capped_fee(100250) == 201

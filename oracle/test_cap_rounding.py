from ledger.fee_cap import capped_fee

def test_half_cent_cannot_pass_the_cap():
    assert capped_fee(250250) == 500

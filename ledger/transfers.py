"""Outgoing transfers (REQ-PAY-201, REQ-PAY-210, REQ-PAY-230)."""
from . import audit
from .auth import require_owner
from .fees import transfer_fee
from .iban import is_valid_iban

DAILY_LIMIT_CENTS = {"basic": 1_000_000, "premium": 2_000_000}  # €10k / €20k


class TransferError(Exception):
    pass


def daily_total(db, account_id: str, day: str) -> int:
    row = db.execute(
        "SELECT COALESCE(SUM(amount_cents), 0) FROM transfers "
        "WHERE from_account = ? AND created_day = ? AND status IN ('pending', 'booked')",
        (account_id, day),
    ).fetchone()
    return row[0]


def create_transfer(db, user_id, account_id, to_iban, amount_cents, kind="sepa",
                    memo=None, idempotency_key=None, day="2026-11-14"):
    require_owner(db, user_id, account_id)
    if idempotency_key:
        prior = db.execute(
            "SELECT id FROM transfers WHERE user_id = ? AND idempotency_key = ?",
            (user_id, idempotency_key),
        ).fetchone()
        if prior:
            return prior[0]
    if amount_cents <= 0:
        raise TransferError("amount must be positive")
    if not is_valid_iban(to_iban):
        raise TransferError("invalid IBAN")
    balance, overdraft, tier = db.execute(
        "SELECT balance_cents, overdraft_cents, tier FROM accounts WHERE id = ?", (account_id,)
    ).fetchone()
    fee = transfer_fee(amount_cents, kind)
    if amount_cents + fee > balance + overdraft:
        raise TransferError("insufficient funds")
    if daily_total(db, account_id, day) + amount_cents > DAILY_LIMIT_CENTS[tier]:
        raise TransferError("daily limit exceeded")
    db.execute(
        "UPDATE accounts SET balance_cents = balance_cents - ? WHERE id = ?",
        (amount_cents + fee, account_id),
    )
    cur = db.execute(
        "INSERT INTO transfers (user_id, from_account, to_iban, amount_cents, fee_cents, kind, status, memo, idempotency_key, created_day) "
        "VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?, ?)",
        (user_id, account_id, to_iban, amount_cents, fee, kind, memo, idempotency_key, day),
    )
    audit.record(db, "transfer.created", user_id, iban=to_iban, amount_cents=amount_cents, kind=kind)
    return cur.lastrowid

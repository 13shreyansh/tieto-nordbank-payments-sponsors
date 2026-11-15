"""Authorisation checks (REQ-SEC-301)."""


class Forbidden(Exception):
    pass


def require_owner(db, user_id: str, account_id: str) -> None:
    row = db.execute("SELECT owner_id FROM accounts WHERE id = ?", (account_id,)).fetchone()
    if row is None or row[0] != user_id:
        raise Forbidden(f"user {user_id} may not access account {account_id}")

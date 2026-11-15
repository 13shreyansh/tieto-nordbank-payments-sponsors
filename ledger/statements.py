"""Monthly statement export (REQ-DATA-502)."""
import csv
import io


def export_csv(db, account_id: str) -> str:
    rows = db.execute(
        "SELECT created_day, to_iban, amount_cents, fee_cents, memo FROM transfers WHERE from_account = ? ORDER BY id",
        (account_id,),
    ).fetchall()
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["day", "to", "amount_cents", "fee_cents", "memo"])
    for r in rows:
        w.writerow(r)
    return out.getvalue()

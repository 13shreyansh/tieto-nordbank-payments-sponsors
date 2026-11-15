"""SQLite storage. Schema lives in migrations/."""
import pathlib
import sqlite3

MIGRATIONS = pathlib.Path(__file__).resolve().parent.parent / "migrations"


def connect(path: str = ":memory:") -> sqlite3.Connection:
    db = sqlite3.connect(path)
    for sql in sorted(MIGRATIONS.glob("*.sql")):
        db.executescript(sql.read_text())
    return db


def seed(db) -> None:
    db.executemany(
        "INSERT INTO accounts (id, owner_id, iban, balance_cents, overdraft_cents, tier) VALUES (?,?,?,?,?,?)",
        [
            ("acc-anna", "u-anna", "FI2112345600000785", 250_000, 0, "basic"),
            ("acc-ben", "u-ben", "FI5542345670000081", 1_200_000, 50_000, "premium"),
        ],
    )

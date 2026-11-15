CREATE TABLE accounts (
  id TEXT PRIMARY KEY,
  owner_id TEXT NOT NULL,
  iban TEXT NOT NULL,
  balance_cents INTEGER NOT NULL,
  overdraft_cents INTEGER NOT NULL DEFAULT 0,
  tier TEXT NOT NULL DEFAULT 'basic'
);
CREATE TABLE transfers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT NOT NULL,
  from_account TEXT NOT NULL,
  to_iban TEXT NOT NULL,
  amount_cents INTEGER NOT NULL,
  fee_cents INTEGER NOT NULL,
  kind TEXT NOT NULL,
  status TEXT NOT NULL,
  memo TEXT,
  idempotency_key TEXT,
  created_day TEXT NOT NULL
);
CREATE TABLE audit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event TEXT NOT NULL,
  user_id TEXT NOT NULL,
  detail TEXT NOT NULL
);

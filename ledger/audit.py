"""Audit trail (REQ-OBS-401). Never write a full IBAN or name to logs."""
import json
import logging

from .iban import mask_iban

log = logging.getLogger("kassa.audit")


def record(db, event: str, user_id: str, **fields) -> None:
    if "iban" in fields:
        fields["iban"] = mask_iban(fields["iban"])
    db.execute(
        "INSERT INTO audit_log (event, user_id, detail) VALUES (?, ?, ?)",
        (event, user_id, json.dumps(fields, sort_keys=True)),
    )
    log.info("%s user=%s %s", event, user_id, json.dumps(fields, sort_keys=True))

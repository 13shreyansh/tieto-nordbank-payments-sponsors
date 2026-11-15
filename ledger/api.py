"""HTTP API for the web client. Synthetic auth: the X-User header is the session user."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import db as dbmod
from .fees import transfer_fee
from .money import format_amount, to_cents
from .transfers import TransferError, create_transfer
from .auth import Forbidden

WEB = Path(__file__).resolve().parent.parent / "web"
ROUTES = {}


def route(method, path):
    def deco(fn):
        ROUTES[(method, path)] = fn
        return fn
    return deco


@route("GET", "/api/fee")
def get_fee(db, user_id, params):
    cents = to_cents(params["amount"])
    fee = transfer_fee(cents, params.get("kind", "sepa"))
    return {"fee_cents": fee, "fee_display": format_amount(fee)}


@route("POST", "/api/transfer")
def post_transfer(db, user_id, params):
    tid = create_transfer(
        db, user_id, params["account_id"], params["to_iban"], to_cents(params["amount"]),
        kind=params.get("kind", "sepa"), memo=params.get("memo"),
        idempotency_key=params.get("idempotency_key"),
    )
    return {"transfer_id": tid, "status": "pending"}


def make_app(db):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype="application/json"):
            data = body if isinstance(body, bytes) else json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _dispatch(self, method):
            url = urlparse(self.path)
            if method == "GET" and not url.path.startswith("/api/"):
                name = "transfer.html" if url.path in ("/", "") else url.path.lstrip("/")
                f = WEB / name
                if f.is_file():
                    ctype = "text/html" if f.suffix == ".html" else "application/javascript"
                    return self._send(200, f.read_bytes(), ctype)
                return self._send(404, {"error": "not found"})
            fn = ROUTES.get((method, url.path))
            if fn is None:
                return self._send(404, {"error": "not found"})
            params = {k: v[0] for k, v in parse_qs(url.query).items()}
            if method == "POST":
                n = int(self.headers.get("Content-Length", 0))
                params.update(json.loads(self.rfile.read(n) or b"{}"))
            try:
                self._send(200, fn(db, self.headers.get("X-User", "u-anna"), params))
            except Forbidden as e:
                self._send(403, {"error": str(e)})
            except (TransferError, ValueError, KeyError) as e:
                self._send(400, {"error": str(e)})

        def do_GET(self):
            self._dispatch("GET")

        def do_POST(self):
            self._dispatch("POST")

    return Handler


def serve(port=8765):
    db = dbmod.connect()
    dbmod.seed(db)
    ThreadingHTTPServer(("127.0.0.1", port), make_app(db)).serve_forever()


if __name__ == "__main__":
    import sys
    serve(int(sys.argv[1]) if len(sys.argv) > 1 else 8765)

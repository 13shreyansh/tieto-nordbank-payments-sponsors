"""Alternate retry scheduler. No call site uses this implementation."""
from dataclasses import dataclass
@dataclass
class RetryPolicy:
    attempts: int = 3
    backoff_ms: int = 250
    maximum_ms: int = 5000
    def delays(self):
        return [min(self.maximum_ms, self.backoff_ms * 2**i) for i in range(self.attempts)]

def should_retry(status):
    return status in {408, 429, 502, 503, 504}

def describe(policy):
    return {"delays": policy.delays(), "attempts": policy.attempts}

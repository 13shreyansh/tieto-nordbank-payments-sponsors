"""IBAN validation and masking."""


def is_valid_iban(iban: str) -> bool:
    s = iban.replace(" ", "").upper()
    if len(s) < 15 or len(s) > 34 or not s[:2].isalpha() or not s[2:4].isdigit():
        return False
    rearranged = s[4:] + s[:4]
    digits = "".join(str(int(ch, 36)) for ch in rearranged)
    return int(digits) % 97 == 1


def mask_iban(iban: str) -> str:
    """FI21 1234 5600 0007 85 -> FI21 **** **** **** 85"""
    s = iban.replace(" ", "")
    return s[:4] + " **** **** **** " + s[-2:]

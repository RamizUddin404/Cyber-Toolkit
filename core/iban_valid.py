#!/usr/bin/env python3
"""Check IBAN format and mod-97 checksum locally; does not verify account existence."""
import re


def validate_iban(value):
    iban = re.sub(r"\s+", "", value).upper()
    if not re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}", iban):
        return False, "Invalid IBAN format or length."
    rearranged = iban[4:] + iban[:4]
    digits = "".join(str(ord(ch) - 55) if ch.isalpha() else ch for ch in rearranged)
    remainder = 0
    for start in range(0, len(digits), 7):
        remainder = int(str(remainder) + digits[start:start + 7]) % 97
    return remainder == 1, "Checksum valid." if remainder == 1 else "Checksum invalid."


def main():
    value = input("Enter IBAN (spaces allowed): ")
    valid, message = validate_iban(value)
    print(("Valid checksum: " if valid else "Not valid: ") + message)
    print("Note: this checks format/checksum only, not whether the bank account exists.")


if __name__ == "__main__":
    main()

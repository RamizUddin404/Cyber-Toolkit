#!/usr/bin/env python3
"""Readable Base64 text encoder/decoder; does not execute decoded content."""
import base64
import binascii


def main():
    print("Base64 Text Utility")
    print("1. Encode UTF-8 text")
    print("2. Decode Base64 to UTF-8 text")
    choice = input("Choose (1/2): ").strip()
    value = input("Text or Base64 value: ")
    try:
        if choice == "1":
            print(base64.b64encode(value.encode("utf-8")).decode("ascii"))
        elif choice == "2":
            decoded = base64.b64decode(value.encode("ascii"), validate=True)
            print(decoded.decode("utf-8"))
        else:
            print("Invalid choice.")
    except (UnicodeError, binascii.Error, ValueError) as exc:
        print(f"Could not process input: {exc}")


if __name__ == "__main__":
    main()

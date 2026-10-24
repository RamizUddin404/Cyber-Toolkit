#!/usr/bin/env python3
"""Base64 and URL-safe Base64 text conversion; decoded output is never executed."""
import base64
import binascii


def main():
    print("Base64 Pro — text only")
    print("1. Standard Base64 encode")
    print("2. Standard Base64 decode")
    print("3. URL-safe Base64 encode")
    print("4. URL-safe Base64 decode")
    choice = input("Choose (1-4): ").strip()
    value = input("Enter text/value: ")
    try:
        if choice == "1":
            result = base64.b64encode(value.encode("utf-8"))
        elif choice == "2":
            result = base64.b64decode(value.encode("ascii"), validate=True)
        elif choice == "3":
            result = base64.urlsafe_b64encode(value.encode("utf-8"))
        elif choice == "4":
            result = base64.urlsafe_b64decode(value.encode("ascii"))
        else:
            print("Invalid choice.")
            return
        print(result.decode("utf-8") if choice in {"2", "4"} else result.decode("ascii"))
    except (UnicodeError, binascii.Error, ValueError) as exc:
        print(f"Could not process input: {exc}")


if __name__ == "__main__":
    main()

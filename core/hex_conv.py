#!/usr/bin/env python3
"""Convert plain UTF-8 text to/from hexadecimal bytes."""


def main():
    print("Hexadecimal Text Converter")
    print("1. Text to hex")
    print("2. Hex to text")
    choice = input("Choose (1/2): ").strip()
    value = input("Enter text/hex: ").strip()
    try:
        if choice == "1":
            print(value.encode("utf-8").hex())
        elif choice == "2":
            print(bytes.fromhex(value).decode("utf-8"))
        else:
            print("Invalid choice.")
    except (UnicodeError, ValueError) as exc:
        print(f"Could not process input: {exc}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Convert plain UTF-8 text to/from binary byte representation."""


def main():
    print("Binary Text Converter")
    print("1. Text to binary")
    print("2. Binary to text")
    choice = input("Choose (1/2): ").strip()
    value = input("Enter text/binary: ")
    try:
        if choice == "1":
            print(" ".join(f"{byte:08b}" for byte in value.encode("utf-8")))
        elif choice == "2":
            bits = value.split()
            if not bits or any(len(bit) != 8 or set(bit) - {"0", "1"} for bit in bits):
                raise ValueError("Enter bytes as 8-bit groups separated by spaces.")
            print(bytes(int(bit, 2) for bit in bits).decode("utf-8"))
        else:
            print("Invalid choice.")
    except (UnicodeError, ValueError) as exc:
        print(f"Could not process input: {exc}")


if __name__ == "__main__":
    main()

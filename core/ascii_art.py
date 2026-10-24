#!/usr/bin/env python3
"""Print a simple text banner without third-party dependencies."""


def main():
    text = input("Enter banner text: ").strip() or "CYBER TOOLKIT"
    if len(text) > 80:
        print("Please use 80 characters or fewer.")
        return
    border = "+" + "-" * (len(text) + 2) + "+"
    print(border)
    print(f"| {text} |")
    print(border)


if __name__ == "__main__":
    main()

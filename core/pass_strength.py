#!/usr/bin/env python3
"""Estimate password strength locally; input is hidden and never stored."""
from getpass import getpass
import string


def estimate_strength(password):
    if not password:
        return "Empty", 0
    score = 0
    score += len(password) >= 12
    score += len(password) >= 16
    score += any(ch.islower() for ch in password)
    score += any(ch.isupper() for ch in password)
    score += any(ch.isdigit() for ch in password)
    score += any(ch in string.punctuation for ch in password)
    if len(password) < 8:
        score = min(score, 1)
    if len(set(password)) <= 3:
        score = min(score, 2)
    label = "Very weak" if score <= 1 else "Weak" if score <= 2 else "Fair" if score <= 3 else "Strong" if score <= 4 else "Very strong"
    return label, score


def main():
    password = getpass("Enter a password to assess locally (input hidden): ")
    label, score = estimate_strength(password)
    print(f"Estimated strength: {label} ({score}/6)")
    print("This is a rough local estimate, not a guarantee against guessing.")


if __name__ == "__main__":
    main()

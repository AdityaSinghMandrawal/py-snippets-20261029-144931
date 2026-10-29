#!/usr/bin/env python3
"""Simple secure-ish password generator."""

import secrets
import string


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print("Passwords:")
    for i in range(5):
        print(f"  {i + 1}. {generate_password()}")

#!/usr/bin/env python3
"""Fibonacci sequence helpers."""


def fib(n: int) -> list[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def fib_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("First 15 Fibonacci numbers:")
    print(fib(15))
    print("Via generator:", list(fib_generator(10)))

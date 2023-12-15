#!/usr/bin/env python3

import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2

    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    f = lambda x: (x**2 + c) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def factorize_rsa_number(number):
    factors = []

    while number > 1:
        factor = pollards_rho(number)
        factors.append(factor)
        number //= factor

    return factors

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                factors = factorize_rsa_number(number)
                print(f"{number}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)


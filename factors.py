#!/usr/bin/env python3

import sys

def factorize(number):
    # Find the smallest divisor
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return number, 1

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                factor1, factor2 = factorize(number)
                print(f"{number}={factor1}*{factor2}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)


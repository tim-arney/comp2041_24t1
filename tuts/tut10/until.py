#! /usr/bin/env python3

"""
Write a Python program, `until.py` which takes as an argument either a line 
number (e.g. `3`) or a regular expression (e.g. `/.[13579]/`) and prints all 
lines given to it by standard input until the given line number, or the first 
line matching the regular expression.
"""

import sys
import re

def main():
    try:
        address = int(sys.argv[1])
    except ValueError:
        address = re.compile(sys.argv[1][1:-1])

    for num, line in enumerate(sys.stdin, start=1):
        if isinstance(address, int):
            if num == address:
                break
        else:
            if address.search(line):
                break

        print(line, end='')

    print(line, end='')

if __name__ == "__main__":
    main()
#! /usr/bin/env python3

"""
Write a Python program, `times.py` which prints a table of multiplications.

Your program will be given the dimension of the table and the width of the columns to be printed. 

For example:

```sh
$ ./times.py 5 5 5
    1     2     3     4     5
    2     4     6     8    10
    3     6     9    12    15
    4     8    12    16    20
    5    10    15    20    25
"""

import sys

def main():
    if len(sys.argv) != 4:
        sys.exit(f"Usage: {sys.argv[0]} <rows> <cols> <width>")

    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        width = int(sys.argv[3])
    except ValueError:
        sys.exit("Arguments must be integers")

    # range([start,[step,]]stop)
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            value = i * j
            print(f"{value:>{width}}", end="")
        print()


if __name__ == '__main__':
    main()
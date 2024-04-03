#! /usr/bin/env python3

"""
Write a Python program `source_count.py` which prints the number of lines of 
C source code in the current directory. In other words, this Python program 
should behave similarly to `wc -l *.[ch]`.
"""

from glob import glob

def main():
    overall_total = 0

    for filename in sorted(glob("*.[ch]")):
        with open(filename) as file:
            total = 0

            # looping over all lines
            for line in file:
                total += 1

            # reading all lines at once
            # lines = file.readlines()
            # total = len(lines)

            overall_total += total
            print(f"{total:>7} {filename}")
    print(f"{overall_total:>7} total")

if __name__ == "__main__":
    main()
#! /usr/bin/env python3

"""
Write a Python program that maps all lower-case vowels (a,e,i,o,u) in its 
standard input into their upper-case equivalents and, at the same time, maps 
all upper-case vowels (A, E, I, O, U) into their lower-case equivalents.
"""

import sys

VOWELS = "aeiou"

def main():
    # naive solution
    # map = dict(zip(VOWELS.lower() + VOWELS.upper(),
    #                VOWELS.upper() + VOWELS.lower()))
    
    # for line in sys.stdin:
    #     for char in line:
    #         if char in map:
    #             char = map[char]
            
    #         print(char, end='')

    # cleaner solution
    map = str.maketrans(VOWELS.lower() + VOWELS.upper(),
                        VOWELS.upper() + VOWELS.lower())
    
    for line in sys.stdin:
        print(line.translate(map), end='')

if __name__ == "__main__":
    main()
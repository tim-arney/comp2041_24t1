#! /usr/bin/env python3

"""
Write a Python program `missing_words.py` which given two files as arguments 
prints, in sorted order, all the words found in file1 but not file2.

You can assume words occur one per line in each file.
"""

import sys
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} <file1> <file2>")

    file1 = Path(sys.argv[1])
    file2 = Path(sys.argv[2])

    if not file1.is_file():
        sys.exit(f"File '{file1}' not found.")
    
    if not file2.is_file():
        sys.exit(f"File '{file2}' not found.")

    words1 = set()

    with open(file1) as f1:
        for word in f1:
            words1.add(word.strip())

    # without a context manager we need to explicitly 
    # close the file afterwards
    # f1 = open(file1)

    # for word in f1:
    #     words1.add(word.strip())

    # f1.close()
    
    words2 = set()

    with open(file2) as f2:
        for word in f2:
            words2.add(word.strip())

    missing_words = words1 - words2
    missing_words = sorted(missing_words)

    for missing_word in missing_words:
        print(missing_word)


if __name__ == "__main__":
    main()
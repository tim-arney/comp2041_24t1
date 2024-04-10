#! /usr/bin/env python3

"""
Write a Python program, `tags.py` which given the URL of a web page fetches it 
by running [wget] and prints the HTML tags it uses.

The tag should be converted to lower case and printed in alphabetical order with 
a count of how often each is used.

Don't count closing tags.

Make sure you don't print tags within HTML comments.
"""

import re
import subprocess
import sys
from collections import Counter

def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <url>")

    url = sys.argv[1]

    process = subprocess.run(["wget", "-q", "-O-", url], capture_output=True, text=True)

    webpage = process.stdout.lower()

    webpage = re.sub(r"<!--[^>]*-->", "", webpage, flags=re.DOTALL)

    tags = re.findall(r"<\s*(\w+)", webpage)
    tag_counts = Counter()

    # Counter already initialises to zero if key not in dict
    # if tag not in tag_counts:
    #     tag_counts[tag] = 0

    for tag in tags:
        tag_counts[tag] += 1

    for tag, count in sorted(tag_counts.items()):
        print(tag, count)


if __name__ == "__main__":
    main()
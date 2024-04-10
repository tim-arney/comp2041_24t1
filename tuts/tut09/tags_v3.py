#! /usr/bin/env python3

"""
Write a Python program, `tags.py` which given the URL of a web page fetches it 
by running [wget] and prints the HTML tags it uses.

The tag should be converted to lower case and printed in alphabetical order with 
a count of how often each is used.

Don't count closing tags.

Make sure you don't print tags within HTML comments.

Add an `-f` option to `tags.py` which indicates the tags are to be printed in 
order of frequency.

Modify `tags.py` to use the `requests` and `beautifulsoup4` modules.
"""

import argparse
from collections import Counter

import requests
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(
                    prog='tags_v2',
                    description='Counts tags in a webpage',
                    epilog='Contact someone else if you need help')

    parser.add_argument('url')           # positional argument
    parser.add_argument('-f', '--frequency',
                        action='store_true',
                        help='order the output by frequency')  # on/off flag

    args = parser.parse_args()

    webpage = requests.get(args.url).text

    soup = BeautifulSoup(webpage, 'html5lib')
    tags = soup.find_all(True)
    tags = [tag.name for tag in tags]

    tag_counts = Counter()

    for tag in tags:
        tag_counts[tag] += 1

    if args.frequency:
        for tag, count in reversed(tag_counts.most_common()):
            print(tag, count)
    else:
        for tag, count in sorted(tag_counts.items()):
            print(tag, count)


if __name__ == "__main__":
    main()



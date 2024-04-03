#! /usr/bin/env python3

"""
Write a Python program, `phone_numbers.py` which given the URL of a web page 
fetches it by running `wget` and prints any strings that might be phone numbers 
in the web page.

Assume the digits of phone numbers may be separated by zero or more spaces or 
hyphens ('-') and can contain between 8 and 15 digits inclusive.

You should print the phone numbers one per line with spaces & hyphens removed.

```sh
$ ./phone_numbers.py https://www.unsw.edu.au
20151028
11187777
841430912571345
413200225
61293851000
57195873179
```
"""

import re
import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <url>")

url = sys.argv[1]
# wget -q -O- {url}
# -q to silence wgets output
# -O- to write the html file to standard output rather than disk
wget = f"wget -q -O- {url}"
process = subprocess.run(wget, shell=True, capture_output=True, text=True)
html = process.stdout

# pattern: '[\d \-]+'
for number in re.findall(r'[\d \-]+', html):
    number = re.sub(r'\D', '', number)
    if 8 <= len(number) <= 15:
        print(number)

if __name__ == "__main__":
    main()
#! /usr/bin/env python3

import sys

num_lines = 10

# parse the command line arguments
if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    arg = sys.argv[1]
    arg = arg[1:]
    try:
        num_lines = int(arg)
    except ValueError:
        # print("-n argument must be an integer", file=sys.stderr)
        # sys.exit(1)
        sys.exit("-n argument must be an integer")
    except Exception as e:
        sys.exit("Some unexpected error occurred:", e)

for n, line in enumerate(sys.stdin, 1):
    # print(line, end='', file=sys.stdout)
    sys.stdout.write(line)
    if n >= num_lines:
        break
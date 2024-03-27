#! /usr/bin/env python3

import sys

num_lines = 10

# parse the command line arguments
if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
    arg = sys.argv.pop(1)
    arg = arg[1:]
    try:
        num_lines = int(arg)
    except ValueError:
        # print("-n argument must be an integer", file=sys.stderr)
        # sys.exit(1)
        sys.exit("-n argument must be an integer")
    except Exception as e:
        sys.exit("Some unexpected error occurred:", e)


# for n, line in enumerate(sys.stdin, 1):
#     # print(line, end='', file=sys.stdout)
#     sys.stdout.write(line)
#     if n >= num_lines:
#         break

def head(stream, n_lines):
    for n, line in enumerate(stream, 1):
        # print(line, end='', file=sys.stdout)
        sys.stdout.write(line)
        if n >= num_lines:
            break


for file in sys.argv[1:]:
    if file == '-':
        # stream = sys.stdin
        print(f'==> stdin <===')
        head(sys.stdin, num_lines)
    else:
        print(f'==> {file} <===')
        try:
            with open(file) as f:
                head(f, num_lines)
        except FileNotFoundError:
            print(f"No such file or directory: {file}", file=sys.stderr)

        # try:
        #     stream = open(file)
        # except FileNotFoundError:
        #     print(f"No such file or directory: {file}", file=sys.stderr)
        #     continue

        # print(f'==> {file} <===')

    # for n, line in enumerate(stream, 1):
    #     # print(line, end='', file=sys.stdout)
    #     sys.stdout.write(line)
    #     if n >= num_lines:
    #         break

    # if stream != sys.stdin:
    #     stream.close()

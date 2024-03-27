#! /usr/bin/env python3

import sys

# __name__ == 'head_q9' 
# when this module is imported, so the code at the very
# bottom won't be invoked.
# test it out by running the `import-head-q9.py` script
# but...
# __name__ == '__main__' 
# when this script is run directly, and the code at the 
# very bottom will be invoked
print(__name__)

def main():
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


    for file in sys.argv[1:]:
        if file == '-':
            print(f'==> stdin <===')
            head(sys.stdin, num_lines)
        else:
            print(f'==> {file} <===')
            try:
                with open(file) as f:
                    head(f, num_lines)
            except FileNotFoundError:
                print(f"No such file or directory: {file}", file=sys.stderr)

def head(stream, n_lines=10):
    for n, line in enumerate(stream, 1):
        # print(line, end='', file=sys.stdout)
        sys.stdout.write(line)
        if n >= n_lines:
            break

if __name__ == "__main__":
    main()
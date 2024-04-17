#! /usr/bin/env python3

import sys

# `chomp` - The Perl function `chomp` removes a single newline from the end of 
# a string (if there is one).
def chomp(string):
    if string[-1] == '\n':
        return string[:-1]
    else:
        return string

# `qw` - The Perl function `qw` splits a string into a list of words.
def qw(string):
    return string.split()


# `die` - The Perl function `die` prints an error message and exits the program.
def die(message):
    sys.exit(f"{sys.argv[0]}: error: {message}")

print(chomp("with two newlines\n\n"), end='')
print(qw("This was a single string"))
die("nothing more to do")




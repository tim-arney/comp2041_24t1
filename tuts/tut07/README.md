# COMP(2041|9044) Week 07 Tutorial

### Q1

In shell we have been using the following hashbang:

```sh
#!/bin/dash
```

```sh
#! /usr/bin/env dash
```

How should we modify this hashbang to use it with python?

```py
#! /usr/bin/env python3
```


### Q2

What version of python should be used in this course?

```sh
$ python3 --version
Python 3.11.2
```


What are the differences between different versions of python?

- python2 and python3 are different languages
- python3 _should_ be forwards compatible, e.g. what you write in 3.9 should run in 3.11
- but _may_ not be backwards compatible, e.g. what you write in 3.11 may not run in 3.9

### Q3

Where can I find the [python3] documentation?

- [Official Docs](https://docs.python.org/3.11/library/index.html)
- `python3; help(object)`
- `python3 -c 'help()'`


### Q4

What is a REPL?

REPL -> Read-Evaluate-Print-Loop

How do you start the python REPL?

```sh
$ python3
```

### Q5

Write a simple version of the `head` command in Python, that accepts an optional command line argument in the form `-n`, where `n` is a number, and displays the first `n` lines from its standard input.

If the `-n` option is not used, then the program simply displays the first ten lines from its standard input.

```sh
# display first ten lines of file2
$ ./head.py < file2
# same as previous command
$ ./head.py -10 < file2
# display first five lines of file2
./head.py -5 < file2
```



### Q6

Modify the `head` program from the previous question so that, as well as handling an optional `-n` argument to specify how many lines, it also handles multiple files on the command line and displays the first `n` lines from each file, separating them by a line of the form `==> FileName <===`.

```sh
# display first ten lines of file1, file2, and file3
$ ./head.py file1 file2 file3
# display first three lines of file1, and file2
$ ./head.py -3 file1 file2
```



### Q7

The following is a Python version of the `cat` program.

```py
#! /usr/bin/env python3

import sys

if len(sys.argv) == 1:
    sys.argv.append("-")

for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            sys.stdout.write(line)

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
```

Write a new version of `cat` so that it accepts a `-n` command line argument and then prints a line number at the start of each line in a field of width 6, followed by two spaces, followed by the text of the line.

The numbers should constantly increase over all of the input files (i.e. don't start renumbering at the start of each file).

```sh
$ ./cat.py -n myFile
     1  This is the first line of my file
     2  This is the second line of my file
     3  This is the third line of my file
         ...
  1000  This is the thousandth line of my file
```



### Q8

Modify the `cat` program from the previous question so that it also accepts a `-v` command line option to display all characters in the file in printable form.

In particular, end of lines should be shown by a `$` symbol (useful for finding trailing whitespace in lines) and all control characters (ascii code less than 32) should be shown as `^X` (where `X` is the printable character obtained by adding the code for 'A' to the control character code). So, for example, tabs (ascii code 9) should display as `^I`.

```sh
$ ./cat -v myFile
This file contains a tabbed list:$
^I- point 1$
^I- point 2$
^I- point 3$
And this line has trailing spaces   $
which would otherwise be invisible.$
```


### Q9

In Python, you can imitate a main function by using the if `__name__ == '__main__'`: construct.

How does this work?

Why is this useful?



### Q10

How can we use regular expressions in python?



### Q11

What is the difference between `search`, `match`, and `fullmatch`?



### Q12

How are Python's regular expressions different from [grep]?



<!-- Links -->
[python3]: https://manpages.debian.org/bookworm/python3-minimal/python3.1.en.html
[grep]: https://manpages.debian.org/jump?q=grep.1
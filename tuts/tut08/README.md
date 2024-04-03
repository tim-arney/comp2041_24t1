# COMP(2041|9044) Week 08 Tutorial

### Q1

What types are avalible as inbuilt types in Python?

- Numeric: `int`, `float`, `complex`
- Text: `str`
- Sequence: `list` (`[]`), `tuple` (`(,)`), `range`
- Set: `set`, `frozenset`
- Mapping: `dict` (`{}`)
- Binary sequence: `bytes`, `bytearray`, `memoryview`

See [Python Docs](https://docs.python.org/3.11/library/stdtypes.html)

### Q2

What other useful types are available with Python's standard library?

See Python Docs, e.g. for [collections](https://docs.python.org/3.11/library/collections.html)

### Q3

Write a Python function `print_dict()` that displays the contents of a dict in the format below:

```
[key] => value
[Andrew] => green
[Anne] => red
[John] => blue
```

```py
def print_dict(the_dict):
    for key in the_dict:
        print(f"[{key}] => {the_dict[key]}")
```
```py
def print_dict(the_dict):
    for key, value in the_dict.items():
        print(f"[{key}] => {value}")
```

Not useful here, but can also...

```py
def print_dict(the_dict):
    for value in the_dict.values():
        print(f"[unknown] => {value}")
```

### Q4

Write a Python program, `times.py` which prints a table of multiplications.

Your program will be given the dimension of the table and the width of the columns to be printed. 

For example:

```sh
$ ./times.py 5 5 5
    1     2     3     4     5
    2     4     6     8    10
    3     6     9    12    15
    4     8    12    16    20
    5    10    15    20    25
$ ./times.py 10 10 3
  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
  9  18  27  36  45  54  63  72  81  90
 10  20  30  40  50  60  70  80  90 100
```



### Q5

Write a Python program `missing_words.py` which given two files as arguments prints, in sorted order, all the words found in file1 but not file2.

You can assume words occur one per line in each file.



### Q6

Write a Python program `source_count.py` which prints the number of lines of C source code in the current directory. In other words, this Python program should behave similarly to `wc -l *.[ch]`. (Note: you are not allowed to use `wc` or other Unix programs from within the Python script). For example:

```sh
$ ./source_count.py
    383 cyclorana.c
    280 cyclorana.h
     15 enum.c
    194 frequency.c
    624 model.c
    293 parse.c
    115 random.c
     51 smooth.c
    132 util.c
     16 util.h
    410 waveform.c
   2513 total
```



### Q7

Write a Python program, `phone_numbers.py` which given the URL of a web page fetches it by running `wget` and prints any strings that might be phone numbers in the web page.

Assume the digits of phone numbers may be separated by zero or more spaces or hyphens ('-') and can contain between 8 and 15 digits inclusive.
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
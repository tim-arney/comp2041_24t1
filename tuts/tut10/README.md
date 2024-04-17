# COMP(2041|9044) Week 10 Tutorial

### Q1

How is the assignment going?

Does anyone have hints or advice for other students?

Has anyone discovered interesting cases that have to be handled?

- Read the [sed] manual.
- Run `sed` with the `--debug` option.


### Q2

Write a Python program, `until.py` which takes as an argument either a line number (e.g. `3`) or a regular expression (e.g. `/.[13579]/`) and prints all lines given to it by standard input until the given line number, or the first line matching the regular expression. For example:

```sh
seq 1 5 | ./until.py 3
1
2
3
```

```sh
seq 1 20 | ./until.py /.3/
1
2
3
4
5
6
7
8
9
10
11
12
13
```

See [until.py](until.py).


### Q3

Write a Python program that maps all lower-case vowels (a,e,i,o,u) in its standard input into their upper-case equivalents and, at the same time, maps all upper-case vowels (A, E, I, O, U) into their lower-case equivalents.
The following shows an example input/output pair for this program:

|Sample Input Data	|Corresponding Output|
|:------------------|:-------------------|
|This is some boring text.|A little foolish perhaps?|
|ThIs Is sOmE bOrIng tExt.|a lIttlE fOOlIsh pErhAps?|

See [vowels.py](vowels.py)


### Q4

These commands both copy a directory tree to a CSE server.

```sh
scp -rp directory1/ z1234567@login.cse.unsw.edu.au:directory2/
rsync -a directory1/ z1234567@login.cse.unsw.edu.au:directory2/
```

What underlies them?

How do they differ?

Why are these differences important?


### Q5

Assumes Linux kernel source tree containing thousand of source files can be found in `/usr/src/linux`

Write a shell script that emails each of the 50,000 source (.c) files to Andrew, each as an attachment to a separate email.

The source files may be anywhere in a directory tree than goes 10+ levels deep.

Please don't run this script, and in general be very careful with such scripts. It is very embarassing to accidentally send thousands of emails.

What assumptions does your script make?

See [email.sh](email.sh).


### Q6

The Perl programming language has a handful of useful functions.
Write a Python module `perl.py` that contains the following functions:

`chomp` - The Perl function `chomp` removes a single newline from the end of a string (if there is one).

`qw` - The Perl function `qw` splits a string into a list of words.

`die` - The Perl function `die` prints an error message and exits the program.

See [perl.py](perl.py).


## Revision questions

The following questions are primarily intended for revision, either this week or later in session.

Your tutor may still choose to cover some of these questions, time permitting.

### Q1

Write a _shell_ script called `rmall.sh` that removes all of the files and directories below the directory supplied as its single command-line argument. The script should prompt the user with `Delete` X`?` before it starts deleting the contents of any directory X. If the user responds `yes` to the prompt, `rmall` should remove all of the plain files in the directory, and then check whether the contents of the subdirectories should be removed. The script should also check the validity of its command-line arguments.


### Q2

Write a shell script called `check` that looks for duplicated student ids in a file of marks for a particular subject. The file consists of lines in the following format:

```
2233445 David Smith 80
2155443 Peter Smith 73
2244668 Anne Smith 98
2198765 Linda Smith 65
```

The output should be a list of student ids that occur 2+ times, separated by newlines. (i.e. any student id that occurs more than once should be displayed on a line by itself on the standard output).


### Q3
Write a Python script `revline.py` that reverses the fields on each line of its standard input.
Assume that the fields are separated by spaces, and that only one space is required between fields in the output.

For example

```sh
./revline.py
hi how are you
i'm great thank you
Ctrl-D
you are how hi
you thank great i'm
```


### Q4

Which one of the following regular expressions would match a non-empty string consisting only of the letters `x`, `y` and `z`, in any order?

1. `[xyz]+`
2. `x+y+z+`
3. `(xyz)*`
4. `x*y*z*`


### Q5

Which one of the following commands would extract the student id field from a file in the following format:

```
COMP3311;2122987;David Smith;95
COMP3231;2233445;John Smith;51
COMP3311;2233445;John Smith;76
```

1. `cut -f 2`
2. `cut -d; -f 2`
3. `sed -e 's/.*;//'`
4. None of the above.


### Q6

Write a Python program `frequencies.py` that prints a count of how often each letter ('a'..'z' and 'A'..'Z') and digit ('0'..'9') occurs in its input. Your program should follow the output format indicated in the examples below exactly.
No count should be printed for letters or digits which do not occur in the input.

The counts should be printed in dictionary order ('0'..'9','A'..'Z','a'..'z').

Characters other than letters and digits should be ignored.

The following shows an example input/output pair for this program:

```sh
./frequencies.py
The  Mississippi is
1800 miles long!
Ctrl-D
'0' occurred 2 times
'1' occurred 1 times
'8' occurred 1 times
'M' occurred 1 times
'T' occurred 1 times
'e' occurred 2 times
'g' occurred 1 times
'h' occurred 1 times
'i' occurred 6 times
'l' occurred 2 times
'm' occurred 1 times
'n' occurred 1 times
'o' occurred 1 times
'p' occurred 2 times
's' occurred 6 times
```


### Q7

A "hill vector" is structured as an ascent, followed by an apex, followed by a descent, where

- the ascent is a non-empty strictly ascending sequence that ends with the apex
- the apex is the maximum value, and must occur only once
- the descent is a non-empty strictly descending sequence that starts with the apex

For example, [1,2,3,4,3,2,1] is a hill vector (with apex=4) and [2,4,6,8,5] is a hill vector (with apex=8). The following vectors are not hill vectors: [1,1,2,3,3,2,1] (not strictly ascending and multiple apexes), [1,2,3,4] (no descent), and [2,6,3,7,8,4] (not ascent then descent). No vector with less than three elements is considered to be a hill.

Write a Python program `hill_vector.py` that determines whether a sequence of numbers (integers) read from standard input forms a "hill vector". The program should write "hill" if the input does form a hill vector and write "not hill" otherwise.

Your program's input will only contain digits and white space. Any amount of whitespace may precede or follow integers.

Multiple integers may occur on the same line.

A line may contain no integers.

You can assume all the integers are positive. The following shows example input/output pairs for this program:

|Sample Input Data	|Corresponding Output|
|:------------------|:-------------------|
| 1 2 4 8 5 3 2     | hill               |
| 1 2               | not hill           |
| 1 3 1             | hill               |
|   3               |                    |
| 1   1             | not hill           |
| 2 4 6 8 10 10 9 7 5 3 1 | not hill     |


### Q8

A list a1, a2, ... an is said to be converging if

```
a1 > a2 > ... > an
```

and

```
for all i ai - 1 - ai > ai - ai + 1
```

In other words, the list is strictly decreasing and the difference between consecuctive list elements always decreases as you go down the list.

Write a Python program converging.py that determines whether a sequence of positive integers read from standard input is converging. The program should write "converging" if the input is converging and write "not converging" otherwise. It should produce no other output.

| Sample Input Data	| Corresponding Output |
|:------------------|:---------------------|
| 2010 6 4 3        | converging           |
| 20                |                      |
| 15                |                      |
| 9                 | not converging       |
| 1000              |                      |
|     100   10      |                      |
|     1             | converging           |
|   6               |                      |
|   5               |                      |
| 2 2               | not converging       |
|  1 2 4 8          | not converging       |

Your program's input will only contain digits and white space. Any amount of whitespace may precede or follow integers.

Multiple integers may occur on the same line.

A line may contain no integers.

You can assume your input contains at least 2 integers.

You can assume all the integers are positive.


### Q9

The weight of a number in a list is its value multiplied by how many times it occurs in the list. Consider the list [1 6 4 7 3 4 6 3 3]. The number 7 occurs once so it has weight 7. The number 3 occurs 3 times so it has weight 9. The number 4 occurs twice so it has weight 8.

Write a Python program heaviest.py which takes 1 or more positive integers as arguments and prints the heaviest.

Your Python program should print one integer and no other output.

Your Python program can assume it it is given only positive integers as arguments

```sh
./heaviest.py 1 6 4 7 3 4 6 3 3
6
./heaviest.py 1 6 4 7 3 4 3 3
3
./heaviest.py 1 6 4 7 3 4 3
4
./heaviest.py 1 6 4 7 3 3
7
```


<!-- Links -->
[sed]: https://www.gnu.org/software/sed/manual/sed.html

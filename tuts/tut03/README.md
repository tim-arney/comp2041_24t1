# COMP(2041|9044) Week 03 Tutorial

### Q1

Assume that we are in a shell where the following shell variable assignments have been performed,
and `ls` gives the following result:

```sh
$ x=2  y='Y Y'  z=ls
$ ls
    a       b       c
```

What will be displayed as a result of the following `echo` commands:


|    |        Command         | Output |
|---:|:-----------------------|:-------|
| a. | `$ echo a   b   c`     | `???`
| b. | `$ echo "a   b   c"`   | `???`
| c. | `$ echo $y`            | `???`
| d. | `$ echo x$x`           | `???`
| e. | `$ echo $xx`           | `???`
| f. | `$ echo ${x}x`         | `???`
| g. | `$ echo "$y"`          | `???`
| h. | `$ echo '$y'`          | `???`
| i. | `$ echo $($y)`         | `???`
| j. | `$ echo $($z)`         | `???`
| k. | `$ echo $(echo a b c)` | `???`


### Q2

The following C program and its equivalent in Python3 all aim to give precise 
information about their command-line arguments.

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("#args = %d\n", argc - 1);

    for (int i = 1; i < argc; i++) {
        printf("arg[%d] = \"%s\"\n", i, argv[i]);
    }

    return 0;
}
```

```py
#!/usr/bin/env python3
from sys import argv

def main():
    print(f"#args = {len(argv) - 1}")
    for index, arg in enumerate(argv[1:], 1):
        print(f'arg[{index}] = "{arg}"')

if __name__ == '__main__':
    main()
```

Assume that these programs are compiled in such a way that we may invoke them 
as `./args`.  Consider the following examples of how it operates:

```sh
$ ./args a b c
#args = 3
arg[1] = "a"
arg[2] = "b"
arg[3] = "c"
$ args "Hello there"
#args = 1
arg[1] = "Hello there"
```

Assume that we are in a shell where the following shell variable assignments have been performed,
and ls gives the following result:

```sh
$ x=2  y='Y Y'  z=ls
$ ls
    a       b       c
```

What will be the output of the following:

1. `./args x y   z`

    ```

    ```

2. `./args $(ls)`

    ```

    ```


3. `./args $y`

    ```

    ```


4. `./args "$y"`

    ```

    ```


5. `./args $(echo "$y")`

    ```

    ```


6. `./args $x$x$x`

    ```

    ```


7. `./args $x$y`

    ```

    ```


8. `./args $xy`

    ```

    ```


### Q3

Imagine that we have just typed a shell script into the file `my_first_shell_script.sh` 
in the current directory. We then attempt to execute the script and observe the following:

```sh
$ my_first_shell_script.sh
my_first_shell_script.sh: command not found
```

Explain the possible causes for this, and describe how to rectify them.


### Q4


Implement a shell script called `seq.sh` for writing sequences of integers onto 
its standard output, with one integer per line. The script can take up to three 
arguments, and behaves as follows:

- `seq.sh LAST` writes all numbers from 1 up to `LAST`, inclusive. For example:

    ``` sh
    $ ./seq.sh 5
    1
    2
    3
    4
    5
    ```

- `seq.sh FIRST LAST` writes all numbers from `FIRST` up to `LAST`, inclusive. 
For example:

    ```sh
    $ ./seq.sh 2 6
    2
    3
    4
    5
    6
    ```

- `seq.sh FIRST INCREMENT LAST` writes all numbers from `FIRST` to `LAST` in 
steps of `INCREMENT`, inclusive; that is, it writes the sequence `FIRST`, 
`FIRST + INCREMENT`, `FIRST + 2*INCREMENT`, ..., up to the largest integer in 
this sequence less than or equal to `LAST`. For example:

    ```sh
    $ ./seq.sh 3 5 24
    3
    8
    13
    18
    23
    ```


### Q5

What is JSON?

Where might I encounter it?

Why can JSON be difficult to manipulate with tools such as grep?

How can a tool like [jq](https://jqlang.github.io/jq/tutorial/) help?


### Q6

Write a shell script, `no_blinking.sh`, which removes all HTML files in the 
current directory which use the blink element:

```sh
no_blinking.sh
Removing old.html because it uses the <blink> tag
Removing evil.html because it uses the <blink> tag
Removing bad.html because it uses the <blink> tag
```


## Q7


Modify the `no_blinking.sh` shell script to instead take the HTML files to be 
checked as command line arguments and, instead of removing them, adding the 
suffix **.bad** to their name:

```sh
no_blinking.sh awful.html index.html terrible.html
Renaming awful.html to awful.html.bad because it uses the <blink> tag
Renaming terrible.html to terrible.html.bad because it uses the <blink> tag
```


### Q8

Write a shell script, `list_include_files.sh`, which for all the C source files 
(`.c` files) in the current directory prints the names of the files they include 
(`.h` files), for example

```sh
list_include_files.sh
count_words.c includes:
    stdio.h
    stdlib.h
    ctype.h
    time.h
    get_word.h
    map.h
get_word.c includes:
    stdio.h
    stdlib.h
map.c includes:
    get_word.h
    stdio.h
    stdlib.h
    map.h
```


### Q9

The following shell script emulates the cat command using the built-in shell commands read and echo:

```sh
#!/bin/sh
while read line
do
    echo "$line"
done
```

1. What are the differences between the above script and the real cat command?
2. Modify the script so that it can concatenate multiple files from the command 
line, like the real cat

(Hint: the shell's control structures — for example, `if`, `while`, `for` — are 
commands in their own right, and can form a component of a pipeline.)


### Q10

The `gzip` command compresses a text file, and renames it to filename.gz. The 
`zcat` command takes the name of a single compressed file as its argument and writes 
the original (non-compressed) text to its standard output.

Write a shell script called `zshow` that takes multiple `.gz` file names as its 
arguments, and displays the original text of each file, separated by the name of 
the file.

Consider the following example execution of zshow:

```sh
zshow a.gz b.gz bad.gz c.gz
===== a =====
... original contents of file "a" ...
===== b =====
... original contents of file "b" ...
===== bad =====
No such file: bad.gz
===== c =====
... original contents of file "c" ...
```


### Q11

Consider the marks data file from last week's tutorial; assume it's stored in a 
file called `Marks`:

```
2111321 37 FL
2166258 67 CR
2168678 84 DN
2186565 77 DN
2190546 78 DN
2210109 50 PS
2223455 95 HD
2266365 55 PS
...
```

Assume also that we have a file called `Student`s that contains the names and 
student ids of for all students in the class, e.g.

```
2166258 Chen, X
2186565 Davis, PA
2168678 Hussein, M
2223455 Jain, S
2190546 Phan, DN
2111321 Smith, JA
2266365 Smith, JD
2210109 Wong, QH
...
```

Write a shell script that produces a list of names and their associated marks, 
sorted by name:

```
67 Chen, X
77 Davis, PA
84 Hussein, M
95 Jain, S
78 Phan, DN
37 Smith, JA
55 Smith, JD
50 Wong, QH
```

Note: there are many ways to do this, generally involving combinations of filters 
such as `cut`, `grep`, `sort`, `join`, etc. Try to think of more than one solution, 
and discuss the merits of each.


### Q12

Implement a shell script, `grades.sh`, that reads a sequence of (studentID, mark) 
pairs from its standard input, and writes (studentID, grade) pairs to its standard 
output. The input pairs are written on a single line, separated by spaces, and the 
output should use a similar format. The script should also check whether the 
second value on each line looks like a valid mark, and output an appropriate 
message if it does not The script can ignore any extra data occurring after the 
mark on each line.

Consider the following input and corresponding output to the program:

**Input**
```
2212345 65
2198765 74
2199999 48
2234567 50 ok
2265432 99
2121212 hello
2222111 120
2524232 -1
```

**Output**
```
2212345 CR
2198765 CR
2199999 FL
2234567 PS
2265432 HD
2121212 ?? (hello)
2222111 ?? (120)
2524232 ?? (-1)
```

To get you started, here is a framework for the script:

```sh
#!/bin/sh
while read id mark
do
    # ... insert mark/grade checking here ...
done
```

Note that the `read` shell builtin assumes that the components on each input line 
are separated by spaces. How could we use this script if the data was supplied 
in a file that used commas to separate the (studentID, mark) components, rather 
than spaces?

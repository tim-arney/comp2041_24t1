# COMP(2041|9044) Week 02 Tutorial

### Q1

Consider the following columnar (space-delimited) data file containing 
(fictional) contact for various CSE academic staff:

```
G Heiser       Newtown      9381-1234
S Jha          Kingsford    9621-1234
C Sammut       Randwick     9663-1234
R Buckland     Randwick     9663-9876
J A Shepherd   Botany       9665-4321
A Taylor       Glebe        9692-1234
M Pagnucco     North Ryde   9868-6789
```

The data is currently sorted in phone number order.

Can we use the [sort](https://manpages.debian.org/jump?q=sort.1) filter to 
re-arrange the data into telephone-book order?
(alphabetically by last name)

If not, how would we need to change the file in order to achieve this?

No, the last name isn't in the same position on each line.  We would need
to modify the input so the last name was in a consistent position.


### Q2

Consider this Unix password file
(usually found in `/etc/passwd`):

```
root:ZHolHAHZw8As2:0:0:root:/root:/bin/dash
jas:iaiSHX49Jvs8.:100:100:John Shepherd:/home/jas:/bin/bash
andrewt:rX9KwSSPqkLyA:101:101:Andrew Taylor:/home/andrewt:/bin/cat
postgres::997:997:PostgreSQL Admin:/usr/local/pgsql:/bin/bash
oracle::999:998:Oracle Admin:/home/oracle:/bin/bash
cs2041:rX9KwSSPqkLyA:2041:2041:COMP2041 Material:/home/cs2041:/bin/bash
cs3311:mLRiCIvmtI9O2:3311:3311:COMP3311 Material:/home/cs3311:/bin/zsh
cs9311:fIVLdSXYoVFaI:9311:9311:COMP9311 Material:/home/cs9311:/bin/bash
cs9314:nTn.JwDgZE1Hs:9314:9314:COMP9314 Material:/home/cs9314:/bin/fish
cs9315:sOMXwkqmFbKlA:9315:9315:COMP9315 Material:/home/cs9315:/bin/bash
```

Provide a command that would produce each of the following results:

1. Display the first three lines of the file

    ```sh
    head -3 /etc/passwd
    ```

2. Display lines belonging to class accounts
    (assuming that class accounts have a username that starts with either "cs", 
    "se", "bi" or "en", followed by four digit)

    ```sh
    grep -E '^(cs|se|bi|en)[0-9]{4}' /etc/passwd
    ```

3. Display the username of everyone whose shell is /bin/bash

    ```sh
    grep -E ':/bin/bash$' passwd
    ```

4. Create a tab-separated file passwords.txt containing only the username and 
    password of each user

    ```sh
    cut -d':' -f1,2 passwd | sed 's/:/\t/' > passwords.txt
    cut -d':' -f1,2 passwd | tr ':' '\t' > passwords.txt
    ```


### Q3

Consider this fairly standard split-into-words technique.

```sh
tr -cs 'a-zA-Z0-9' '\n' < someFile
tr -cs 'abcde...ABCDE...0123...' '\n' < someFile
tr -cs '[:alnum:]' '\n' < someFile
```

Basic usage is:

```sh
tr [options] string1 string2
```

Explain how this command works.
What does each argument do?

-c option specifies the complement of string1
-s option "squeezes" repeated occurences of characters in string2 to a single occurrence
'a-zA-Z0-9' is all alphanumeric characters
'\n' is the replacement character


### Q4

What is the output of each of the following pipelines if the text:

```
this is big Big BIG
but this is not so big
```

is supplied as the initial input to the pipeline?

1. `tr -d ' ' | wc -w`

    `tr` deletes spaces from each line, so each line is effectively a word.
    `wc` gives us the `-w` "word count"
    Output should be 2.

2. `tr -cs '[:alpha:]' '\n' | wc -l`

    `tr` splits words onto their own line
    `wc` counts the number of `-l` lines
    Output should be 11.


3. `tr -cs '[:alpha:]' '\n' | tr '[:lower:]' '[:upper:]' | sort | uniq -c`

    `tr` will split words to lines
    `tr` will convert all alphabetical characters to uppercase
    `sort` will sort lexicographically
    `uniq` will provide a count of each unique line (i.e. word)

    Note: 'uniq' does not detect repeated lines unless they are adjacent.  You may want to sort the input first, or use 'sort -u' without 'uniq'.

### Q5

Consider a file containing (fake) zIDs and marks in COMP1511:

```
4279700|61
4212240|59
4234024|57
4286024|50
4270657|75
4227010|52
4299716|84
4236088|74
4245033|87
4222098|46
4228842|85
4209182|96
4276270|61
4224421|72
4207416|76
```

and another file containing (fake) zIDs and marks in COMP2041:

```
4200549|92
4283960|77
4203704|48
4261741|43
4224421|67
4223809|75
4276270|80
4279700|68
4233865|61
4207416|56
4209669|71
4209182|70
4213591|49
4236221|53
4201259|91
```

1. Can the files be used as-is with the join command?
    If not, what needs to be changed?

    Important:  FILE1  and  FILE2  must  be  sorted on the join fields.

    So no, they need to be sorted first.

    ```sh
    sort -t'|' -k1,1 q5-1511.txt > 1511-sorted.txt
    sort -t'|' -k1,1 q5-2041.txt > 2041-sorted.txt
    ```

2. Write a `join` command which prints the marks in COMP1511 and COMP2041 of 
    everyone who did both courses.

    ```sh
    join -t'|' 1511-sorted.txt 2041-sorted.txt
    ```

    or:

    ```sh
    join -t'|' -j 1 1511-sorted.txt 2041-sorted.txt
    join -t'|' -1 1 -2 1 1511-sorted.txt 2041-sorted.txt 
    ```


3. Write another `join` command which prints the marks in COMP1511 and COMP2041 
    of everyone, across both files, with `--` in the case where a student didn't 
    do a particular subject.

    ```sh
    join -t'|' -a 1 -a 2 -e '--' -o auto 1511-sorted.txt 2041-sorted.txt 
    ```

    or:

    ```sh
    join -t'|' -a 1 -a 2 -e '--' -o 0,1.2,2.2 1511-sorted.txt 2041-sorted.txt 
    ```

4. Write a shell pipeline which prints the marks in COMP1511 and COMP2041 of 
    everyone who did both courses,
    sorted by their COMP1511 mark in ascending order,
    then by their COMP2041 mark in descending order.

    ```sh
    join -t'|' 1511-sorted.txt 2041-sorted.txt | sort -t'|' -k2,2n -k3,3nr
    ```


### Q6

Consider a file containing tab-separated benchmarking results for 20 programs, 
in three different benchmarks, all measured in seconds.

```
program1	08	03	05
program2	14	03	05
program3	17	08	10
program4	15	11	05
program5	16	10	24
program6	15	09	17
program7	15	06	10
program8	17	10	17
program9	12	07	08
program10	09	04	16
program11	11	03	24
program12	16	11	20
program13	16	08	17
program14	08	07	06
program15	06	06	05
program16	12	05	08
program17	09	05	10
program18	06	06	06
program19	14	09	22
program20	16	04	24
```

1. Write a `sort` command which sorts by the results in the second benchmark, 
    then by the results in the first benchmark.

    ```sh
    sort -k3,3n -k2,2n q6.txt
    ```

2. Write a `sort` command which sorts by the results in the third benchmark, 
    then by the program number.

    ```sh
    sort -k4,4n -k1.8,1n q6.txt
    ```

3. Write a `sed` command which removes the leading zeroes from the benchmark 
    times.

    ```sh
    sed 's/\t0/\t/g' q6.txt
    ```

4. Write a `sed` command which removes the benchmark results from `program2` 
    through `program13`.

    ```sh
    sed '/^program2\b/,/^program13\b/d' q6.txt
    ```

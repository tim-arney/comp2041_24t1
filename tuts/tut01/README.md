# COMP(2041|9044) Week 01 Tutorial

### Q1

- What is your tutor's name and e-mail?

    Tim Arney - t.arney@unsw.edu.au

- How long have they been at UNSW?

    For about 2 years

- What are they studying?

    Master of IT

- Do they have a pet?

    No

- What is 1 interesting thing about them?



### Q2

- What are your class mates's names,
- What are they each studying,
- What is 1 interesting thing about each of them?

### Q3

What is an operating system?

### Q4

What operating systems are being used in your house/tutorial room?

macOS

### Q5

What operating system(s) do CSE lab computers run?

```sh
$uname -a
Linux vx23 6.1.0-17-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.69-1 (2023-12-30) x86_64 GNU/Linux
```

---

### Regular Expressions (Regex)

Regex = regular expression

| Character | Meaning | Example
|:---------:|:-------:|:-------:|
`.` | any character | `.`: 'a', '1', ' '
`*` | 0 or more repetitions | `a*`: '', 'a', 'aa', 'aaa', ...
`?` | 0 or 1 occurrences | `a?`: '', 'a'
`+` | 1 or more repetitions | `a+`: 'a', 'aa', 'aaa', ...
`^` | anchor for start of string | '^abc'
`$` | anchor for end of string | 'abc$'
`{n}` | n repetitions | `a{4}`: 'aaaa'
`{n, m}` | repeating from n to m times | `a{2, 4}`: 'aa', 'aaa', 'aaaa'
`[]` | any character in this set | `[abc]`: 'a', 'b', 'c'; `[a-c]`: 'a', 'b', 'c'
`[^]` | any character not in this set | `[^abc]`: 'd', '1', ' '
`\` | escape character | `\+`: '+'
`|` | alternating/union/or | `abc|def`: 'abc', 'def'
`()` | group things together | `(abc)*`: '', 'abc', 'abcabc', 'abcabcabc', ...
`\s` | any whitespace character | ' ', tab, newline
`\S` | any non-whitespace character | 'a', '1', '.'
`\w` | any word character | `[a-zA-Z0-9_]`
`\d` | any digit



---

### Q6

Write a regex to match:

- C preprocessor commands in a C program source file.

    #include ....
    #define ....

    `^#`

- All the lines in a C program except preprocessor commands.

    `^[^#]|^$`

- All lines in a C program with trailing white space (one or more white space at the end of line).

    `\s+$`

- The names "Barry", "Harry", "Larry" and "Parry".

    `[BHLP]arry`

- A string containing the word "hello" followed, some time later, by the word "world".

    `hello.*world`

- The word "calendar" and mis-spellings where 'a' is replaced with 'e' or vice-versa.

    `c[ae]l[ae]nd[ae]r`

- A list of positive integers separated by commas, e.g. 2,4,8,16,32

    ```
    ([1-9][0-9]*|0)(,([1-9][0-9]*|0))*
    ^\d+(,\d+)*
    ```

- A C string whose last character is newline.

    `"[^"]*\\n"`


### Q7

When should you use:

- `fgrep` / `grep -F`

    Same, but `fgrep` is deprecated.  Just do string matching, rather than 
    regular expressions.  Good to use if you know you don't want regex as it's 
    safer.

- `grep` / `grep -G`

    Same.  Do basic regular expressions.

- `egrep` / `grep -E`

    Same, but `egrep` is deprecated.  Use extended regular expressions.  What
    you want most of the time.

- `pgrep` / `grep -P`


### Q8

grep takes many options (see the manual page for [grep](https://manpages.debian.org/jump?q=grep.1)).

```sh
man 1 grep
```

Give 3 (or more) simple/important options grep takes and explain what they do.


1. `-i`: ignores case
2. `-v`: inverts matches


### Q9

Why does this command seem to be taking a long time to run:

```sh
grep -E hello
```

Reading from stdin as no file arguments supplied - waiting for user input.

### Q10

Why won't this command work:

```sh
grep -E int main program.c
```

`int` is the pattern, `grep` will think `main` is a file.

```sh
grep -E 'int main' program.c
```

### Q11

Give five reasons why this attempt to search a file for HTML paragraph and break tags may fail.

```sh
grep <p>|<br> /tmp/index.html
```

Give a `grep` command that will work.

1. Missing `-E` for extended regex which gives us alternation `|`.
2. No quotes around pattern, `<`, `>`, `|` are special to shell.
3. Not case insensitive, `<p>` and `<P>` should be both be valid.
4. Doesn't account for stuff in tags, e.g. `<p style="...">`
5. Doesn't account for spaces within tags, e.g. `<p >`

### Q12

For each of the regular expression below indicate how many different strings the pattern matches and give some example of the strings it matches.

If possible these example should include the shortest string and the longest string.

- `Perl`
- `Pe*r*l`
- `Full-stop.`
- `[1-9][0-9][0-9][0-9]`
- `I (love|hate) programming in (Perl|Python) and (Java|C)`

| Regexp | Shortest Match | Longest Match | Other Examples
|:------:|:--------------:|:-------------:|:--------------:|
`Perl` | Perl | Perl | none
`Pe*r*l` | Perl | Peeeee...rrrr.....l | Perl, Peerl, Peerrl, ...
`Full-stop.` | Full-stopa | Full-stopa | Full-stopb, Full-stopa!, ...
`[1-9][0-9][0-9][0-9]` | 4 digits | 4 digits | 1000, 1001, ..., 9999
`I (love\|hate) programming in (Perl\|Python) and (Java\|C)` | I love programming in Perl and C | ... | ...


### Q13

This regular expression `[0-9]*.[0-9]*` is intended to match floating point numbers such as '42.5'
Is it appropriate?

No

### Q14

What does the command `grep -Ev .` print and why?

Give an equivalent `grep -E` command with no options, in other words: without the `-v`.

Prints empty lines.  Can achieve the same with:

```sh
grep -E '^$'
```

### Q15

Write a `grep -E` command which will print any lines in a file `ips.txt` containing an IP address in the range `129.94.172.1` to `129.94.172.25`

```sh
grep -E '129\.94\.172\.([1-9]|1[0-9]|2[0-5])' ips.txt
```

### Q16

For each of the scenarios below

- give a regular expression to match this class of strings
- describe the strings being matched using an English sentence

In the examples, the expected matches are highlighted in bold.

- encrypted password fields (including the surrounding colons) in a Unix password file entry, e.g

    ```
    root:ZHolHAHZw8As2:0:0:root:/root:/bin/bash
    jas:nJz3ru5a/44Ko:100:100:John Shepherd:/home/jas:/bin/zsh
    andrewt:ugGYU6GUJyug2:101:101:Andrew Taylor:/home/jas:/bin/dash
    ```

    `:[^:]+:`

- positive real numbers at the start of a line (using normal fixed-point notation for reals, _not_ the kind of scientific notation you find in programming languages), e.g.

    ```
    3.141 value of Pi
    90.57 maximum hits/sec
    half of the time, life is silly
    0.05% is the legal limit
    42 - the meaning of life
    this 1.333 is not at the start
    ```

    `^([1-9][0-9]*|0)(\.[0-9]*)?`

- Names as represented in this file containing details of tute/lab enrolments:

    ```
    2134389|Wang, Duved Seo Ken         |fri15-spoons|
    2139656|Undirwaad, Giaffriy Jumis   |tue13-kazoo|
    2154877|Ng, Hinry                   |tue17-kazoo|
    2174328|Zhung, Yung                 |thu17-spoons|
    2234136|Hso, Men-Tsun               |tue09-harp|
    2254148|Khorme, Saneu               |tue09-harp|
    2329667|Mahsin, Zumel               |tue17-kazoo|
    2334348|Trun, Toyin Hong Recky      |mon11-leaf|
    2336212|Sopuvunechyunant, Sopuchue  |mon11-leaf|
    2344749|Chung, Wue Sun              |fri09-harp|
    ...
    ```

    `[^|,]+, [^|]+`

- Names as above, but without the trailing spaces (difficult).
    
    _Hint_: what are given names composed of, and how many of these things can there be?
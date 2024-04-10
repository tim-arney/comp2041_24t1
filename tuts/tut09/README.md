# COMP(2041|9044) Week 09 Tutorial

### Q1

_Assignment Tips:_

1. Trust `2041 eddy`, its behaviour is almost certainly correct. But if in doubt...
2. Try `sed -E`, it should confirm the behaviour.  Otherwise...
3. Consult the [sed] manual, it has all the answers.

Below are the current assignment autotests.

Discuss what these print and why:

#### subset 0: quit

```sh
seq 42 44 | 2041 eddy 1q
2041 eddy 10q < /usr/share/dict/words
seq 41 43 | 2041 eddy 4q
seq 90 110 | 2041 eddy /.1/q
2041 eddy '/r.*v/q' < /usr/share/dict/words
yes | 2041 eddy 3q
```

#### subset 0: print

```sh
seq 41 43 | 2041 eddy 2p
head /usr/share/dict/words | 2041 eddy 3p
seq 41 43 | 2041 eddy -n 2p
2041 eddy -n 42p < /usr/share/dict/words
head -n 1000 /usr/share/dict/words | 2041 eddy -n '/z.$/p'
```

#### subset 0: substitute

```sh
seq 1 5 | 2041 eddy 's/[15]/zzz/'
seq 1 5 | 2041 eddy 's/[15]/zzz/g'
echo "Hello Andrew" | 2041 eddy 's/e//'
echo "Hello Andrew" | 2041 eddy 's/e//g'
```

#### subset 1: addresses

```sh
seq 1 5 | 2041 eddy '$d'
seq 42 44 | 2041 eddy 2,3d
seq 10 21 | 2041 eddy 3,/2/d
seq 10 21 | 2041 eddy /2/,7d
seq 10 21 | 2041 eddy /2/,/7/d
```

#### subset 1: substitute
```sh
seq 1 5 | 2041 eddy 'sX[15]XzzzX'
```

#### subset 1: multiple commands

```sh
seq 1 5 | 2041 eddy '4q;/2/d'
```

#### subset 1: -f

```sh
echo "4q" > commands.script
echo "/2/d" >> commands.script
seq 1 5 | 2041 eddy -f commands.script
```

#### subset 1: input files

```sh
seq 1 2 > two.txt
seq 1 5 > five.txt
2041 eddy '4q;/2/d' two.txt five.txt
```

#### subset 1: whitespace

```sh
seq 24 42 | 2041 eddy ' 3, 17  d  # comment'
```

#### subset 2: -i

```sh
seq 1 5 > five.txt
2041 eddy -i /[24]/d five.txt
cat five.txt
```

#### subset 2: multiple commands

```sh
echo 'Punctuation characters include . , ; :' | 2041 eddy 's/;/semicolon/g;/;/q'
```


### Q2

Write a Python program, `tags.py` which given the URL of a web page fetches it by running [wget] and prints the HTML tags it uses.

The tag should be converted to lower case and printed in alphabetical order with a count of how often each is used.

Don't count closing tags.

Make sure you don't print tags within HTML comments.

```sh
./tags.py https://www.cse.unsw.edu.au
a 141
body 1
br 14
div 161
em 3
footer 1
form 1
h2 2
h4 3
h5 3
head 1
header 1
hr 3
html 1
img 12
input 5
li 99
link 3
meta 4
noscript 1
p 18
script 14
small 3
span 3
strong 4
title 1
ul 25
```

Note the counts in the above example will not be current - the CSE pages change almost daily.

[tags_v1.py](tags_v1.py)


### Q3

Add an `-f` option to `tags.py` which indicates the tags are to be printed in order of frequency.

```sh
./tags.py -f https://www.cse.unsw.edu.au
head 1
noscript 1
html 1
form 1
title 1
footer 1
header 1
body 1
h2 2
hr 3
h4 3
span 3
link 3
small 3
h5 3
em 3
meta 4
strong 4
input 5
img 12
br 14
script 14
p 18
ul 25
li 99
a 141
div 161
```

[tags_v2.py](tags_v2.py)


### Q4

Modify `tags.py` to use the `requests` and `beautifulsoup4` modules.

[tags_v3.py](tags_v3.py)


### Q5

If you fell like a harder challenge after finishing the challenge activity in the lab this week have a look at the following websites for some problems to solve using regexp:

- [https://regex101.com/quiz](https://regex101.com/quiz)
- [https://alf.nu/RegexGolf](https://alf.nu/RegexGolf)

<!-- Links -->
[wget]: https://manpages.debian.org/jump?q=wget.1
[sed]: https://www.gnu.org/software/sed/manual/sed.html
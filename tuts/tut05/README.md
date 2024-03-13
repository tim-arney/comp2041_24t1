# COMP(2041|9044) Week 05 Tutorial

### Q1

The assignment specification doesn't fully explain the assignment - what can I do?

Incomplete spec is _intentional_.  Big part of the assignment is understanding 
what `git` does, either by researching `git` and/or exploring the `2041 pushy` 
reference implementation.

Of course, you're always welcome to ask questions on the forum, but you _may_ 
get vague answers.  Sorry!

And there'll be help sessions!


### Q2

How hard are the subsets?

- Subset 0, once you understand the basics of the assignment is _fairly_ 
straightforward
- Subset 1, is a little harder
- Subset 2, very hard...will take time!

### Q3

What does `git init` do?
How does this differ from `pushy-init`?

`pushy-init` creates a `.pushy` directory, if it does not exist

- _may_ initialise other things within `.pushy`, but this is entirely up to you
- you can store anything you like inside `.pushy`

`git init` creates a `.git` directory, if it does not exist

Both effectively initialise an empty repository.


### Q4

What do `git add file` and `pushy-add file` do?

Takes a snapshot of `file` and updates the index (including if the file no 
longer exists).


### Q5

What is the index in `pushy` (and `git`), and where does it get stored?

Adding a file to the repository is a two step process.

First it needs to be "added" to the index, sometimes called the "stage" or 
"staging area", and then "committed" to the repository.

The index records the state of a file as of when it was last added.

The index lives within your `.pushy` (or `.git`) sub-directory, in whatever 
format you want it to be.


### Q6

What is a commit in `pushy` (and `git`), and where does it get stored?

A commit preserves the state of all files in the index at that moment in time.

It must be stored somewhere in `.pushy`, but how and where within `.pushy` is 
up to you.


### Q7

Apart from the `pushy-*` scripts what else do you need to submit (and give an example)?

You need to submit 10 test files, `test00.sh` ... `test09.sh`.

See example [test00.sh](q7/test00.sh)

### Q8

You work on the assignment for a couple of hour tonight.
What do you need to do when you are finished?

`give` it.

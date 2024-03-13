#! /usr/bin/env dash

# Write a shell function print_message that, given an optional exit status and 
# a message:

# If no exit status is given the program should print a warning
# If an exit status is given the program should print an error and exit the 
# program

command=$(basename $0)

print_message() {
    if [ $# -eq 1 ]; then
        echo "${command}: $1"
    elif [ $# -eq 2 ]; then
        echo "${command}: $2"
        exit "$1"
    else
        echo "No message given..."
    fi
}

# print_message "This is a warning"
# print_message 1 "This is an error"
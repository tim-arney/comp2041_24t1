#! /usr/bin/env dash

# Make sure our scripts are in the PATH
PATH="$PATH:$(pwd)"

# Source our print_message.sh script
. print_message.sh

# Call the function defined in print_message.sh
print_message
print_message "This is a warning"
print_message 1 "This is an error"

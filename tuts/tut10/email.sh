#! /usr/bin/env dash

directory="/Users/tarney/code/unsw/ts/linux-master"

for c_file in $(find "$directory" -type f -name '*.c'); do
    # don't actually call mutt, just echo the command to email
    echo mutt -s 'Linux C File' -a "$c_file" -- andrewt@unsw.edu.au
done


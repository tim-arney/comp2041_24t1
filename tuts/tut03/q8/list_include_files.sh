#! /usr/bin/env dash

for file in *.c; do
    includes=$(grep -E '^#include' "$file" | sed -E 's/#include[[:space:]]*["<]([^">]+)[">].*/\1/')

    if [ -z "$includes" ]; then
        continue
    fi

    echo "$file includes:"

    for include in $includes; do
        echo "    $include"
    done
done
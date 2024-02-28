#! /usr/bin/env dash

FIRST=1
INCREMENT=1
LAST=

if [ "$#" -eq 1 ]; then
    LAST="$1"
elif [ "$#" -eq 2 ]; then
    FIRST="$1"
    LAST="$2"
elif [ "$#" -eq 3 ]; then
    FIRST="$1"
    INCREMENT="$2"
    LAST="$3"
else
    echo "Usage: $0 [first [increment]] last" >&2
fi

while [ "$FIRST" -le "$LAST" ]; do
    echo "$FIRST"
    FIRST=$((FIRST + INCREMENT))
done

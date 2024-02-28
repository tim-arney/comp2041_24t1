#! /usr/bin/env dash

while read id mark _
do
    # ... insert mark/grade checking here ...
    echo -n "$id "

    if ! [ "$mark" -eq "$mark" ] 2> /dev/null || [ "$mark" -lt 0 ] || [ "$mark" -gt 100 ]; then
        echo "?? ($mark)"
        continue
    fi

    # if [ "$mark" -lt 0 ] || [ "$mark" -gt 100 ]; then
    #     echo "?? ($mark)"
    #     continue
    # fi

    if [ "$mark" -ge 85 ]; then
        echo "HD"
    elif [ "$mark" -ge 75 ]; then
        echo "DN"
    elif [ "$mark" -ge 65 ]; then
        echo "CR"
    elif [ "$mark" -ge 50 ]; then
        echo "PS"
    else
        echo "FL"
    fi
done
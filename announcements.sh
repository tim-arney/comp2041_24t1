#! /usr/bin/env dash

# TODO:

# - make time difference more precise/accurate
# - ensure output is sorted by date
# - avoid temp files?
# - duplicate checks?

if [ ! -f deadlines ]; then
    echo "No deadlines file found"
    exit 1
fi

overdue="$(mktemp)"
upcoming="$(mktemp)"
trap 'rm "$overdue" "$upcoming"' INT HUP QUIT TERM EXIT

echo
echo -n "Now: "
date +"%a %b %d, %T"

sort -t, -k2,2 deadlines | uniq |
while IFS=, read -r task due _; do

    if [ -z "$task" ]; then
        continue
    fi

    # echo "$task $due"

    print_due=$(date -d "$due" +"%a %b %d, %T")
    date_diff=$(( ($(date -d "$due" +%s) - $(date +%s)) / (60*60*24)))
    # echo "$task | $print_due | $date_diff"

    days="days"
    if [ "$date_diff" -eq 1 ]; then
        days="day"
    fi

    if [ "$date_diff" -lt -5 ]; then
        continue
    elif [ "$date_diff" -lt 0 ]; then
        echo "$task: $print_due ($date_diff ${days})" >> "$overdue"
    else
        echo "$task: $print_due ($date_diff ${days})" >> "$upcoming"
    fi
done

echo
echo "------------- overdue ---------------"
echo
cat "$overdue"

echo
echo "------------- upcoming --------------"
echo
cat "$upcoming"

echo
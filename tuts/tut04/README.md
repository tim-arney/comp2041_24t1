# COMP(2041|9044) Week 04 Tutorial

### Q1
### Q2
### Q3
### Q4
### Q5
### Q6

```sh
mlalias cs2041.wed15c 2> /dev/null | 
sed -n '/Addresses/,/Owners/p' | 
head -n -1 | 
tail -n +2 | 
sed -E 's/^\s*//; s/\s*$//' | 
grep -E 'z[0-9]{7}' | 
cut -d@ -f1
```

### Q7

```sh
acc z5417087 | 
sed -n '/^$/,/^$/p' | 
cut -d: -f2 | tr ',' '\n' | 
sed -nE 's/.*([A-Z]{4}[0-9]{4})t[0-3]_Student.*/\1/p'
```

### Q8

```sh
#! /usr/bin/env dash

mlalias cs2041.wed15c 2> /dev/null |
sed -n '/Addresses/,/Owners/p' |
head -n -1 |
tail -n +2 |
sed -E 's/^\s*//; s/\s*$//' |
grep -E 'z[0-9]{7}' |
cut -d@ -f1 |
while read zid; do
  acc "$zid" |
  sed -n '/^$/,/^$/p' |
  cut -d: -f2 | tr ',' '\n' |
  sed -nE 's/.*([A-Z]{4}[0-9]{4})t[0-3]_Student.*/\1/p'
done |
sort | uniq -c | sort -nr
```

### Q9
### Q10
### Q11

```sh
#! /usr/bin/env dash

program="$1"

echo "$PATH" |
tr ':' '\n' |
while read directory; do
  path="${directory}/${program}"
  if [ -x "$path" ]; then
    # echo "found: $path"
    ls -l "$path"
    exit
  fi
done

echo "$program not found"
```

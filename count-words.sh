#!/bin/bash 
# Count words starting with the given letter in a range of lengths

# Fun tidbit: this will print every letter from 's' to 'e'
#for i in {s..e} do echo "$i"; done

if [ $# != 3 ]; then echo "usage: $0 [first-letter] [shortest-length] [longest-length]"; exit 1; fi

echo "Words starting with $1"
echo "######################"
for i in $(seq $2 $3); do echo -n "$i letters:" && ./word-search.py $1 -l $i | wc -l; done
echo "######################"

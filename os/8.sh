#!/bin/bash
for file in "$@"
do
    if [ -f "$file" ]; then
        echo "$file is a file"
        wc -l "$file"
    elif [ -d "$file" ]; then
        echo "$file is a directory"
    else
        echo "$file not found"
    fi
done


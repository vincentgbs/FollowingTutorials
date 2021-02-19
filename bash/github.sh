#!/bin/bash
### Mac script

COUNTER=20
until [  $COUNTER -lt 10 ]; do
    # add a line to the test file
    echo "adding a line" >> log.txt
    git add .
    git commit -m "Adding a line"

    # remove the last line from the test file
    sed -i '' -e '$ d' log.txt
    git add .
    git commit -m "Removing a line"

    let COUNTER-=1
done

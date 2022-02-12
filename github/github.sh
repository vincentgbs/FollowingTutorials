#!/bin/bash
### Mac script

today=$(date '+%Y-%m-%d')
last=$(tail -n 1 log.txt)

if [ "$today" = "$last" ]
then
    echo "Already completed"
else
    echo "Running Github script"
    COUNTER=5
    until [  $COUNTER -lt 1 ]; do
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

    # remove the date from the test file
    sed -i '' -e '$ d' log.txt
    # add the last run date to the file
    echo $today >> log.txt

    git push origin master
fi

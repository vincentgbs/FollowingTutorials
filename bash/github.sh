# add a line to the test file
echo "adding a line" >> log.txt

# remove the last line from the test file
sed -i '' -e '$ d' log.txt

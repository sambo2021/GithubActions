#!/usr/bin/env bash

regex="^(fix|feat|chore):\\s+[a-zA-Z0-9 ]+\\S$"
commits=$(git log main..release/QA --oneline --pretty=format:"%s")
while IFS= read -r commit; do
    echo $commit
    if [[ "$commit" =~ $regex ]]; then
        echo "The commits are valid"
    else
        echo "The commit: $commit is not valid"
        exit 1
    fi
done <<< "$commits"


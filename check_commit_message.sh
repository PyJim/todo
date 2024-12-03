#!/bin/bash

# Define the commit message format regex
COMMIT_MESSAGE_REGEX="^(feat|fix|docs|style|refactor|test|chore): [A-Z].+$"

# Get the latest commit message
LATEST_COMMIT_MESSAGE=$(git log -1 --pretty=%B)

# Check if the commit message matches the regex
if [[ ! "$LATEST_COMMIT_MESSAGE" =~ $COMMIT_MESSAGE_REGEX ]]; then
  echo "Error: Latest commit message does not follow the required format."
  echo "Commit message must match the pattern: $COMMIT_MESSAGE_REGEX"
  echo "Examples:"
  echo "  feat: Add a new feature"
  echo "  fix: Correct a bug in the code"
  echo "  docs: Update documentation"
  exit 1
else
  echo "Commit message follows the required format."
fi


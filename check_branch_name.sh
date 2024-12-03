#!/bin/bash

# Define the branch naming convention regex
BRANCH_NAME_REGEX="^(feature|bugfix|hotfix|release|chore)\/[a-z0-9._-]+$"

# Get the current branch name from CircleCI
CURRENT_BRANCH=$(echo "$CIRCLE_BRANCH")

# Check if the branch name matches the regex
if [[ ! "$CURRENT_BRANCH" =~ $BRANCH_NAME_REGEX ]]; then
  echo "Error: Branch name '$CURRENT_BRANCH' does not follow the naming convention."
  echo "Branch names must follow the pattern: $BRANCH_NAME_REGEX"
  exit 1
else
  echo "Branch name '$CURRENT_BRANCH' follows the naming convention."
fi


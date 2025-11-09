#!/bin/bash

# Script to update contribution file with current timestamp
# This ensures daily changes to trigger GitHub contribution count

# Create contrib.txt file if it doesn't exist
if [ ! -f "contrib.txt" ]; then
    touch contrib.txt
    echo "Created contrib.txt file"
fi

# Append current timestamp to the contribution file
echo "Contribution at: $(date -u)" >> contrib.txt

# Optional: Add multiple entries per day to make it look more natural
# Uncomment the lines below if you want to add multiple entries per day
# for i in {1..3}; do
#   sleep 1
#   echo "Contribution $i at: $(date -u)" >> contrib.txt
# done

echo "Successfully updated contrib.txt with timestamp"
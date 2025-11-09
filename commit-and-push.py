#!/usr/bin/env python3
"""
Script to update contribution file with current timestamp
This ensures daily changes to trigger GitHub contribution count
"""

import os
from datetime import datetime

def update_contribution_file():
    """Append current timestamp to the contribution file"""
    # Create contrib.txt file if it doesn't exist
    if not os.path.exists("contrib.txt"):
        open("contrib.txt", "w").close()
        print("Created contrib.txt file")
    
    # Append current timestamp to the contribution file
    with open("contrib.txt", "a") as f:
        f.write(f"Contribution at: {datetime.utcnow()}\n")
    
    # Optional: Add multiple entries per day to make it look more natural
    # Uncomment the lines below if you want to add multiple entries per day
    # import time
    # for i in range(1, 4):
    #     time.sleep(1)
    #     f.write(f"Contribution {i} at: {datetime.utcnow()}\n")
    
    print("Successfully updated contrib.txt with timestamp")

if __name__ == "__main__":
    update_contribution_file()
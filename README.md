# ntlmbrutal

**ntlmbrutal** is a Python-based brute-force tool designed to test NTLM-enabled endpoints by attempting username and password combinations. The script leverages `curl` with NTLM authentication to send requests to a specified endpoint, and it identifies valid username/password pairs based on the size of the HTTP response. This tool is intended for security professionals performing penetration tests and red team assessments.

## Features

- **Username and Password Combination Testing**: Reads from `usernames.txt` and `passwords.txt` files to perform authentication attempts for each username-password pair.
- **Single Output File**: Stores all results in a single `results.txt` file with the attempted credentials and whether they were valid (True or False).
- **Random Delay (Jitter)**: Includes a configurable delay (jitter) between requests to avoid detection by rate-limiting or monitoring systems. The delay is random between a specified minimum and maximum (set in milliseconds).
- **Automatic Cleanup**: Deletes temporary files created during the testing process.

## Usage

1. Place your `usernames.txt` and `passwords.txt` files in the same directory as the script. Each file should contain one username or password per line in the correct order.
2. Adjust the `min_delay` and `max_delay` variables at the top of the script to control the random delay between requests.
3. Run the script with the NTLM-enabled endpoint URL as an argument:

   ```bash
   python ntlmbrutal.py <URL>
   python ntlmbrutal.py http://example.com

This command will attempt NTLM authentication using each username-password combination from the files, and it will output the results in results.txt.

## Requirements

- Python 3.x
- curl must be installed on the system

## Disclaimer

This tool is intended for use by security professionals with proper authorization. Unauthorized use of this tool against systems without permission is illegal and unethical.


    

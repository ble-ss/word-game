import sys
import select

def get_user_input(timeout_seconds):
    print(f"Enter something within {timeout_seconds} seconds:")

    # Use select to implement a timeout for input
    rlist, _, _ = select.select([sys.stdin], [], [], timeout_seconds)

    if rlist:
        user_input = sys.stdin.readline().strip()
        print("User input:", user_input)
    else:
        print("Timeout reached. Program terminated.")

# Call the function to get user input with a timeout of 5 seconds
get_user_input(5)


#printing header

import subprocess

cmd = "figlet Word Game"

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print(result.stdout)


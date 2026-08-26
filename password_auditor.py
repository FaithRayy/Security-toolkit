import sys
import os
import getpass

# Check wordlist to avoid common passwords
def is_common_passowrd(pswd, wordList):
    cwd = os.getcwd()
    path = os.path.join(cwd, wordList)

    if not os.path.exists(path):
        return
    
    with open(wordList, "r") as f:
        if pswd in f.read():
            return True

def main(password):

    strengthCheck = False

    # If statements each check for complexity 
    if len(password) < 12:
        print("Use 12 characters minimum for all your passwords")
        strengthCheck = True
    if not any(char.islower() for char in password):
        print("Add a lowercase character")
        strengthCheck = True
    if not any(char.isupper() for char in password):
        print("Add an uppercase character")
        strengthCheck = True
    if not any(char.isdigit() for char in password):
        print("Add a number character")
        strengthCheck = True
    if not any(not char.isalnum() and not char.isspace() for char in password):
        print("Add a symbol character")
        strengthCheck = True

    # Uses the "rockyou.txt" wordlist to check if the given password is common
    if is_common_passowrd(password, "rockyou.txt"):
        print("WARNING: THIS IS A COMMON PASSWORD!")
        strengthCheck = True

    # If none of the above if-statements ran, the password has good complexity
    if not strengthCheck:
        print("You have a strong password!")


if __name__ == "__main__":
    args = sys.argv

    # Cannoot pass any additional arguments
    if len(args) > 1:
        print("Error: Do not pass the password as a command-line argument.", file=sys.stderr)
        print("Usage: python script.py (you will be prompted for the password)", file=sys.stderr)
        sys.exit(1)

    try:
        # Prompt the user securely (input will be hidden as they type)
        password = getpass.getpass("Enter potential password to audit: ")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(1)
        
    if not password:
        print("Error: Password cannot be empty.", file=sys.stderr)
        sys.exit(1)
        
    if " " in password:
        print("Error: Password must not contain spaces.", file=sys.stderr)
        sys.exit(1)

    main(password)


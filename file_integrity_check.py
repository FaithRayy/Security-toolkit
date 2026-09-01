import hashlib
import sys
import os

# Create a new SHA-256 hash for the corresponding txt file
def create_hash(text_file):
    hash_object = None
    new_hash_file = text_file.replace(".txt", "(hash_256).txt")
    
    with open (text_file, "r") as f:
        hash_object = hashlib.sha256((f.read()).encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    
    with open (new_hash_file, "w") as f:
        f.write(hex_dig)
    
    print("Hash file created.")

def compare_hashes(text_file, hash_path):
    hash_object = None
    hash_file = None

    # Open text file and calculate its hash valaue   
    with open (text_file, "r") as f:
        hash_object = hashlib.sha256((f.read()).encode("utf-8"))
    text_hash = hash_object.hexdigest()

    # Open and read the existing hash file
    with open(hash_path, "r") as f:
        hash_file = f.read()

    # Return True or False for text hash and hash file are equal
    return text_hash == hash_file
    

def main(text_file):
    cwd = os.getcwd()

    # Check if the given text file exists
    file_path = os.path.join(cwd, text_file)
    if not os.path.exists(file_path):
        print("This file does not exist within this directory")
        return

    hash_name = text_file.replace(".txt", "(hash_256).txt")
    hash_path = os.path.join(cwd, hash_name)

    # Check if corresponding hash file exists
    if os.path.exists(hash_path):
        if compare_hashes(text_file, hash_path):
            print("The file has not had any changes.")
        else:
            print("The file has been changed.")
    else:
        response = input("A corresponding hash does not exist for this file.\nWould you like to create a new one? Y or N\n")
        while True:
            if response == "Y":
                create_hash(text_file)
                break
            elif response == "N":
                break
            else:
                response = input("Please input Y or N\n")
            
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("You need to pass the name of the text file only")

    text_File = " ".join(args[1:])

    main(text_File)


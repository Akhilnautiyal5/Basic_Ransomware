import os
from cryptography.fernet import Fernet

def decryption(files, KEY_FILE, EXTENSION):
    HEADER = b'encrypted::'
    decryped_files = []
    with open(KEY_FILE, "rb") as theKey:
        key = theKey.read()

    for file in files:
        if not file.endswith(EXTENSION):
            continue               
        with open(file, "rb") as thefile:
            contents = thefile.read()
            
        if not contents.startswith(HEADER):
            print("continue")
            continue
        
        decrypted_content = Fernet(key).decrypt(contents[len(HEADER):])
        with open(file, "wb") as thefile:
            thefile.write(decrypted_content)

        new_file_path = file.replace(EXTENSION, '')
        os.rename(file, new_file_path)
        decryped_files.append(new_file_path)
        
    return decryped_files


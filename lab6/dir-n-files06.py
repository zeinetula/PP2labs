import string
import os

directory = r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab6\letters"

for letter in string.ascii_uppercase:
    open(os.path.join(directory, f"{letter}.txt"), "w").close()
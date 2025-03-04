import os

path = r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab6\test.txt"


if os.path.exists(path):
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist")
import os

filename = r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab6\delete.test.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted")
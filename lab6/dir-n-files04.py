filename = r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab6\test.txt"

with open(filename, "r") as file:
    print("Number of lines:", sum(1 for line in file))
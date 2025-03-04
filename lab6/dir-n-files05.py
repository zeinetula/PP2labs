filename = r"C:\Users\ayanz\OneDrive\Desktop\PP2labs\lab6\output.txt"

data = ["apple", "banana", "cherry"]

with open(filename, "w") as file:
    for item in data:
        file.write(item + "\n")
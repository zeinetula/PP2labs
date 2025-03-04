import os

path = "." 
print("Directories:", [os.path.realpath(d) for d in os.listdir(path)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])

print(os.listdir())
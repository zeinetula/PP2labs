import os

path = "." 
print([os.path.realpath(d) for d in os.listdir(path)])
print(os.listdir())
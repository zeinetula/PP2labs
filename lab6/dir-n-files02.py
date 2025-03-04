import os

print(os.access(os.getcwd(),os.F_OK))
print(os.access(os.getcwd(),os.R_OK))
print(os.access(os.getcwd(),os.W_OK))
print(os.access(os.getcwd(),os.X_OK))
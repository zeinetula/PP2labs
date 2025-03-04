a = "AAbbCCc"
num_uppers = sum(1 for c in a if c.isupper())
num_lowers = sum(1 for c in a if c.islower())
print("Uppercase:", num_uppers)
print("Lowercase:", num_lowers)

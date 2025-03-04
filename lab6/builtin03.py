a = input()

def func(a):

    rev = "".join(reversed(a))

    return rev==a
print (func(a))
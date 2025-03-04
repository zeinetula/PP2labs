from functools import reduce
a=[1,2,3,4,5]
res=reduce(lambda x,y:x*y,a)
print (res)

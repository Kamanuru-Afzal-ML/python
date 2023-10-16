from functools import reduce
lis=[x for x in range(10)]
total=reduce(lambda x,y:x+y,lis)
print(total)


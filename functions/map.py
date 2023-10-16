lis=[x for x in range(10)]
double=tuple(map(lambda x:x*2,lis))
print(double)

evens=list(filter(lambda x:x%2==0,lis))
print(evens)


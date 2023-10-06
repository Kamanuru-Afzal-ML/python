l=[x for x in range(1,20)]
new=list(map(lambda x:x*2,l))
fil=filter(lambda x:x>10,new)
print(new)
print(list(fil))

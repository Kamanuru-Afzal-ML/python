tup=(4,5,1,2,9,3)
print(tup)
print(sorted(tup)) #returing in a list
print(tuple(sorted(tup)))

listtup=tuple([x for x in tup])
print(listtup)

for i in listtup:
    print(i)

print(max(listtup))


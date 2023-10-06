l=[x for x in range(1,20)]
max=min=second_max=l[0]
for i in l:
    if i>max:
        second_max=max
        max=i
    else:
        min=i
print(min,max,second_max)
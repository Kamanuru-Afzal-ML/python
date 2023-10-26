l=[1,3,1,5,6,2]
fmax=l[0]
smax=l[0]
for i in range(1,len(l)):
    if(fmax<l[i]):
        fmax=l[i]
    if(fmax>l[i] and smax<l[i]):
        smax=l[i]
print(fmax,smax)
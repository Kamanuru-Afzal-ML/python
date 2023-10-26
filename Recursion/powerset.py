def powerSet(lis):
    n=len(lis)
    power_set=[]
    for i in range(2**n):
        subset=[]
        for j in range(n):
            if (i>>j) & 1:
                print("here:",'i:',i,'j:',j,'and i>>j:',i>>j)
                subset.append(lis[j])
        power_set.append(subset)
    print(power_set)

l=[1,2,3]
powerSet(l)
lis=[x for x in range(10,21)]
total=0
for i in lis:
    total+=i
print(total//len(lis))
print(sum(lis)//len(lis)) #by usinf sum()

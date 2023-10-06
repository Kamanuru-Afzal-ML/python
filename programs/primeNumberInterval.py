start=int(input('Enter starting value:'))
end=int(input('Enter ending value:'))
for i in range(start, end+1):
    prime=0
    for j in range(1,i+1):
        if(i%j==0):
            prime+=1
    if(prime==2):
        print(i)


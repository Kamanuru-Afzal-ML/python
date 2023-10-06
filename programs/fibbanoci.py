num=int(input('Enter number'))-2
a=0
b=1
print(a)
print(b)
while num!=0:
    print(a+b)
    a,b=b,b+a
    num-=1

def sumof(num):
    if(num<=0):
        return num
    return num%10+sumof(num//10)
n=123
print(sumof(n))

def sumofparameter(n,sum):    #(10,0) --> (9,10+0)-->(8,10+9)-->(7,19,7)
    if(n==0):
        print(sum)
    else:
        sumofparameter(n-1,sum+n)
sumofparameter(10,0)


def sumbyfun(num):
    if(num==1):
        return num
    else:
        return num+sumbyfun(num-1)

print(sumbyfun(10))


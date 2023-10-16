def repeat(counter,name):
    if(counter<0):
        return
    print(name)
    repeat(counter-1,name)
repeat(10,'abbu')

def increse(num):
    if num==0:
        return
    print(num)
    increse(num-1)
increse(4)

def one_n(o,n):
    if(o>=n):
        return
    print(o)
    one_n(o+1,n)
one_n(1,10)

def factorial(num):
    if(num==0):
        return 1
    else:
        return num*factorial(num-1)   
#5*factorial(4)====>4*factorial(3)====>3*factorial(2)#2*factorial(1)===>1*factorial(0) return

print("Factorial of 5:",factorial(5))

#reversing number
#123
def reverse(num):
    if(num<=0):
        return 1
    else:
        print(num%10)
        return reverse(num//10)
         
print("reverse of 123",reverse(123))


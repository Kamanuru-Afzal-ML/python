def febbanoci(num):            #f(5)=f(4)+f(3)
    if num<= 0:
        return num
    else:
        return febbanoci(num-2)+febbanoci(num-1)

for i in range(10):
    print(febbanoci(i))
'''
n=5
        f(5)
    f(4)+f(2)
f(3)+f(2)                   
f(2)+f(1)   f(1)+f(0)
f(1)    
'''
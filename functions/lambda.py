add=lambda x,y:x+y 
print(add(9,1))          #positonal arguments

diff=lambda x=10,y=2:x-y   #default arguments
print(diff())           

test=lambda x,y,z:y            #keyword arguments
print(test(y=0,x=1,z=2))

arg=lambda *args:sum(args)
print(arg(1,2,3,4))
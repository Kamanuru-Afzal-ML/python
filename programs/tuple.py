#tuple packing
tup=('red','white','black')
lis=['red=','white','black']
#tuple unpacking
[a,b,c]=lis
# (a,b,c)=tup
print(a)
print(type(a))
print(a)
test=(1,2,3,4,[5,6,7],8,9)
#bascially tuple is ummutable,inside list is ummutable r mutable
print(test)
test[4][0]=0 
print(test)

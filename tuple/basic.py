t=(1)       #consider as single value not tuple
print(type(t))   
t1=(1,)    #tuple
print(type(t1))
nested_tuple=(1,2,3,(4,4))
print(nested_tuple[3][0])
nested_tuple_list=(1,2,3,[4,5,6])
nested_tuple_list[3][0]=5
print(nested_tuple_list)

#tuple packing
tup=('red','green','blue')
print(tup)

#tuple unpacking
(r,g,b)=tup
print(r,g)

email='afzalkamanuru@gmail.com'
name,domain=email.split('@')
print(name,domain)

#slicing 
print(nested_tuple[::-1])

#tuple concatenation and repitition

tuple_concat=(1,2,3)+(4,5,6)
print(tuple_concat)

tuple_repit=('a',)*5
print(tuple_repit)

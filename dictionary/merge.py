D1={'name':'abbu','surname':'kamanuru'}
D2={'age':23}
D1.update(D2)
print(D1)
D1.update({'gender':'male'})
print(D1)


#removing item
print(D1.pop('gender'))
print(D1.popitem())        # removes last item
#after removing
print(D1)
D1.clear()   #remove all items
print(D1)

E=['emp1','emp2','emp3','emp4','emp5','emp6','emp7']
Fields={'name':'emp_name','surname':'EMP_name'}
D=dict.fromkeys(E,Fields)
print(D)
print(D['emp1']['name'])
print(D['emp2'].get('name'))

for k,v in D.items():
    print(k,v)
    
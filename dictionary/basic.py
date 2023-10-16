D={'name':'afzal','surname':'kamanuru','email':'kamanuruafzal@gmail.com'}
print(D.keys())     # to get keys from disctionary
print(D.values())   # to get values from disctionary

DL=[('age',3),('gender','male')]
print(dict(DL))

DT=([23,24],[90,91])
print(DT)

D_keyword_arg=dict(city='bangalore',pincode='516269')
print(D_keyword_arg)

L1=['number','string','float']
L2=[1,'maplelabs',1.2]
D_ZIP=dict(zip(L1,L2))
print(D_ZIP)

#when can take any immutable iterate as key 
D_I={(1,2):'numberGroup',True:1}
print(D_I)

#if it is a mutable iterate it will give error-->TypeError: unhashable type: 'list'
# D_L={[1,2]:'numberGroup'}
# print(D_L)

print(D.get('name'))  # it prints value of that key
print(D.get('IAMNOTINDICT'))   # it prints none







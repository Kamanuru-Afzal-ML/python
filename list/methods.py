l=[x for x in range(30)]
l.append(30)
newList=[31,32,33,34,35,36,37,38,39]
l.extend(newList)
l[0]=100
l.insert(0,0)
print(l.pop())
print(l)
print(l.pop(2))  #deleting the element at the index of 2

print(l.count(1)) #count of occured element in the list
l.clear()   #deleting list
print(l)
l=[9,2,34,3]
l.sort() #sorting the list
print(l)
print(l.index(34))
l.reverse() #reverse the list
print(l)

#slicing the list
newList=['apple','orange','banana',1,2,3,4]
#list[start:end:step]
print(newList[::])
print(newList[::-1]) # reverse the list
print(newList[::2]) #even indexed elements printed
nestedList=['apple','orange','ban',[1,2,3,4]]
print(nestedList[1][0])

#membership operators
print('apple' in nestedList)
print('leeche' not in nestedList)

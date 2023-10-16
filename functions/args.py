def myFun(*args):
    return args
lis=[x for x in range(20,1,-2)]
print(myFun(lis))

def myFun2(**kwargs):
    print(kwargs)
d={'name':'afzal','lname':'kamanuru'}
myFun2(name='afzal',lname='kamanuru')

myFun2()

def docString():
    '''this is for documentation purposes
       to add extra information
       in a multle lines to describing the function'''
    print("hello world")
print(docString())
help(docString) #to access documentation 
print(docString.__doc__)



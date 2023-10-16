def outer(a,b):
    def inner(x,y):
        return x*y
    return inner(a,b)
result=outer            #assigning function to varaible 
print(result(3,9))

# Jump table is a dictionary of functions to be called on demand.
def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
function_store={'s':sum,'d':diff,'m':multiply,'D':divide}
print(function_store['s'](1,2))
print(function_store['d'](1,2))
print(function_store['m'](1,2))
print(function_store['D'](1,2))

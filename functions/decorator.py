def decorate_func(func):
    def wrapper():
        print("Decorating func")
        func()
    wrapper()

@decorate_func    #decorate_me=decoarate_func(decorate_me)
def decorate_me():
    print("MAIN")

def sum(fun):
    def wrapper(*args,**kwargs):
        print("Before")
        fun(*args, **kwargs)
        print("After")
    return wrapper

@sum       
def getValue(x):
    print(x)
getValue(1)

from functools import wraps

def pow_of_two(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args, **kwargs)
        print(result)
        return result**2
    return wrapper
def double_it(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args, **kwargs)
        print(result*2)
        return result*2
    return wrapper
@double_it
@pow_of_two
def number(val):
    return val
print(number(5))

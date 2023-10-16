def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
print(say_hello())
class Parent:
    def __init__(self):
        self.__x=10
    def Show(self):
        print(self.__x)
obj=Parent()
print(obj.__x)
print(obj.Show())
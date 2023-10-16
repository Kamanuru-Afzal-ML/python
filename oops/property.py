class Person:
    def __init__(self,name):
        self.hidden_name=name
    def get_name(self):
        print('getting name')
        return self.hidden_name
    def set_name(self,name):
        print('setting name',name)
        self.hidden_name=name
    def del_name(self):
        print('deling name',self.hidden_name)
        del self.hidden_name
    #property making
    user=property(get_name,set_name,del_name,doc="name of the person")
p=Person('Afzal')
print(p.user)
p.user="AZA"
del p.user

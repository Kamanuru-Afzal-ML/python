class Vehicle:
    def decription(self):
        print("Vehicle class")
class Car(Vehicle):
    def decription(self):
        print('Car class')
v=Vehicle()
v.decription()
c=Car()
c.decription()
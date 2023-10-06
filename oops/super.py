class Vehicle:
    def __init__(self,color):
        self.color = color
    def description(self):
        print("Car manufactured with ",self.color,"color")
class Car(Vehicle):
    def __init__(self,color,style):
        super().__init__(color)            #it invokes base class constructor
        self.style=style
    def description(self):
        super().description() #it invokes base class method description
        print("car  color:",self.color)
        print("car style:",self.style)
punch=Car('black','hatchback')
punch.description()

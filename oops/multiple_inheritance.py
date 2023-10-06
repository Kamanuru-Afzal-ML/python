class GroundVehicle:
    def __init__(self):
        pass
    def drive(self):
        print("Drives on road")
class FlyingVehicle:
    def fly(self):
        print("Fly on  sky")
class WaterVehicle:
    def ship(self):
        print("drive on water")
class vehicle(GroundVehicle,FlyingVehicle,WaterVehicle):
    pass
v=vehicle()
v.drive()
v.fly()
v.ship()

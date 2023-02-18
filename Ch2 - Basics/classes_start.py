#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed 

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")       
        self.wheels = 4
        self.door = 4
        self.enginetype = enginetype

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else: 
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype    

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas",True) 

print(mc1.wheels)
print(car1.enginetype)
print(car2.door)    
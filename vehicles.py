class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride(self, duration):
        self.distance += duration * self.speed


class Bike(Vehicle):
    def __init__(self):
        super().__init__(15)

class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.top_speed = 2 * self.speed


b = Bike()
b.ride(2)
print(b.distance)

c = Car()
c.ride(2)
print(c.distance)
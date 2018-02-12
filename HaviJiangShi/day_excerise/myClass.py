class MyClass:
    name = 'li'

    def sayHello(self, year):
        print('hello %s %s' %(self.name, year))

mc = MyClass()
mc.name = 'wang'
mc.sayHello(5)
print(mc)

class Car:
    speed = 0
    def drive(self, distance):
        time = distance / self.speed
        print(time)

car1 = Car()
car1.speed = 10
car1.drive(100)


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('need %s hour' %(distance / self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('need %f fuels' %(distance * self.fuel))
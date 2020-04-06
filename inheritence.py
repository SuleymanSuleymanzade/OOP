
class Car:
    def __init__(self):
        self.coordinates = (0,0)
    
    def move(self, x, y):
        self.coordinates = (self.coordinates[0] + x, self.coordinates[1] + y)

class BMW(Car):
    def __init__(self, model):
        super(BMW, self).__init__()
        self.model = model 

    def move(self, x, y):
        super(BMW, self).move(x, y)
        super(BMW, self).move(x, y)


car = Car()

bmw = BMW("5-th series")

print(bmw.coordinates)

bmw.move(2, 4)

print(bmw.coordinates)


import abc

class Car(metaclass = abc.ABCMeta):
    def __init__(self):
        self.coordinates = (0,0)
    
    @abc.abstractmethod    
    def move(self, x, y):
        pass

class BMW(Car):
    def __init__(self, model):
        super(BMW, self).__init__()
        self.model = model 

    def move(self, x, y):
        self.coordinates = (self.coordinates[0] + x, self.coordinates[1] + y)


car = Car()

bmw = BMW("5-th series")

print(bmw.coordinates)

bmw.move(2, 4)

print(bmw.coordinates)


import abc

class Car(metaclass = abc.ABCMeta):
    def __init__(self):
        self._coordinates = (0,0)
    
    @abc.abstractmethod    
    def move(self, x, y):
        pass

class BMW(Car):
    def __init__(self, model):
        super(BMW, self).__init__()
        self.model = model 


    def __str__(self):
        return f"{__class__.__name__} {self._coordinates}"

    def move(self, x, y):
        self._coordinates = (self._coordinates[0] + x, self._coordinates[1] + y)

class Audi(Car):
    def __init__(self, model):
        super(Audi, self).__init__()
        self.model = model 
        self.__speed_coefficient = 3

    @property 
    def speed_coefficient(self):
        return self.__speed_coefficient 

    @speed_coefficient.setter 
    def speed_coefficient(self, coef):
        self.__speed_coefficient = coef 

    def __str__(self):
        return f"{__class__.__name__} {self._coordinates}"

    def move(self, x, y):
        self.coordinates = (self._coordinates[0] + x*self.__speed_coefficient,
            self._coordinates[1] + y*self.__speed_coefficient)

def main():
    bmw = BMW("5-th series")
    audi = Audi('a4')
    bmw.move(2, 4)
    audi.move(2,4)
    print(bmw)
    print(audi)
    audi.speed_coefficient = 7
    audi.move(2,4)
    print(audi)
if __name__ == "__main__":
    main()
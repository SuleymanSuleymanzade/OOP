import abc

class Vehicle(metaclass = abc.ABCMeta):
	def __init__(self, x, y):
		self.x = x 
		self.y = y 

	@abc.abstractmethod
	def move(self, x, y):
		pass 


class Car(Vehicle):
	def __init__(self, x, y):
		super(Car, self).__init__(x, y)

	def move(self, x, y):
		self.x += x * 0.8
		self.y += y * 0.8 
	
	def __str__(self):
		return f"<Car {(self.x, self.y)}>"

	@staticmethod
	def change_oil(km):
		s = 0
		for i in km:
			s += i * 1.2

		if s > 100:
			return True
		return False  



class Motorcycle(Vehicle):
	def __init__(self, x, y):
		super(Motorcycle, self).__init__(x, y)

	def move(self, x, y):
		self.x += x * 1.2
		self.y += y * 1.2 

	def __str__(self):
		return f"<Motorcycle {(self.x, self.y)}>"


def main():
	m = Motorcycle(2, 3)
	c = Car(2, 3)
	print(c)
	print(m)

	m.move(3, 4)
	c.move(3, 4)
	
	print(" -- after move (3, 4) -- ")
	
	print(c)
	print(m)

	c_oil = Car.change_oil([2,3,6,5,4,6,1,5])
	print(c_oil)

if __name__ == "__main__":
	main()




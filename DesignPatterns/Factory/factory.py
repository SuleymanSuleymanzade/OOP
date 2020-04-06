import abc 

class Car(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def drive(self):
		pass

class Audi(Car):
	def drive(self):
		print('driving: Audi car')

class BMW(Car):
	def drive(self):
		print('driving: BMW car')
		

class CarFactory:
	def drive(self, car_object):
		return eval(car_object)().drive()


#=================== Client ================

def main():

	cf = CarFactory()
	
	cf.drive("BMW")
	cf.drive("Audi")


if __name__ == "__main__":
	main()






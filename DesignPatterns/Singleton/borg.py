class Borg:
	
	__shared_dictionary = {'x': 5}

	def __init__(self):
		self.__dict__ = self.__shared_dictionary
	'''
	@property
	def x(self):
		return x 

	@x.setter
	def x(self, new_x):
		self.x = x 
	'''
	

p1 = Borg()
p2 = Borg()

print(f"p1.x: {p1.x}")
p1.x = 555

print(f"p2.x: {p2.x}")

	
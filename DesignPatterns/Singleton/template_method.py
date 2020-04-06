import abc 


class Template(metaclass = abc.ABCMeta):
	
	def __init__(self):
		pass

	@abc.abstractmethod
	def move(self):
		pass

	@abc.abstractmethod
	def jump(self):
		pass

	@abc.abstractmethod
	def turn(self):
		pass

	def go_back(self):
		for _ in range(2):
			self.turn()
		self.move()
		self.move()
		self.jump()

class Hook(Template):
	def __init__(self):
		super(Hook, self).__init__()

	def jump(self):
		print('hook has been jumped')

	def move(self):
		print('hook has been moved')

	def turn(self):
		print('turned 90 degree')

class Robot(Template):
	def __init__(self):
		super(Robot, self).__init__()

	def jump(self):
		print('Robot has been jumped')

	def move(self):
		print('Robot has been moved')

	def turn(self):
		print('Robot 90 degree')

h = Hook()
r = Robot()

h.go_back()
print()
r.go_back()

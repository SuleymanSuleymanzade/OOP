
class Singleton:
	__instance = None 
	@classmethod 
	def get_instance(cls):
		if cls.__instance is None:
			cls.__instance = Singleton(cls)
		return cls.__instance 

			
	def __init__(self):
		if not self.__instance:
			return
		self.get_instance()


s1 = Singleton()
s2 = Singleton()

print(s1.x)
print(s2.x)
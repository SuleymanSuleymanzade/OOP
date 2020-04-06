
class Singleton:
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance 
	


s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)

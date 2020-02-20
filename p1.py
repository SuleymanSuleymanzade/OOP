class Meta(type):
	def __new__(self, class_name, bases, attr):
		#print(attr)
		arr = {}
		for item, value in attr.items():
			if item.startswith('__'):
				arr[item] = value
			else:
				arr[item.upper()] = value

		print(arr)
		return type(class_name, bases, arr)

class Dog(metaclass = Meta):
	x = 5
	y = 7 

dog = Dog()

print(dog)
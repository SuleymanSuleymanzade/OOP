from typing import List

class Person:

	def __init__(self, name:str = "unknown", surname = "unknown"):
		self.__name = name
		self.__surname = surname
		self.__x = 0
		self.__y = 0
		self.__bus = None

	@property
	def name(self):
		return self.__name 

	@property 
	def surname(self):
		return self.__surname

	@property
	def coordinates(self):
		return (self.__x, self.__y)
	
	def set_coordinates(self, x, y):
		if type(x) in (int, float):
			self.__x = x
			self.__y = y

	def move(self, x, y):
		self.__x += x
		self.__y += y

	def get_on_bus(self, bus):
		bus.add_person(self)
		self.__bus = bus 

	def get_name_of_bus(self):
		if self.__bus:
			return self.__bus.number
		else:
			return "not in bus" 

	def __str__(self):
		return f" {self.name} {self.surname}, {self.coordinates}>"


class Bus:
	def __init__(self, number:str = "000"):
		self.__number = number 
		self.__persons = []
		self.__x = 0 
		self.__y = 0

	@property
	def number(self):
		return self.__number

	@number.setter
	def number(self, new_number):
		self.__number = new_number

	def add_person(self, person):
		self.__persons.append(person)

	def remove_person(self, name:str, surname:str):
		for per in self.__persons:
			if per.name == name and per.surname == surname:
				self.__persons.remove(per)

	def show_passengers(self):
		for per in self.__persons:
			print(per.name)

	@property
	def coordinates(self):
		return (self.__x, self.__y)

	def move(self, x, y):
		self.__x += x
		self.__y += y
		for person in self.__persons:
			person.move(x, y)

	def __str__(self):
		return f"<{self.__class__.__name__}: {self.__number}>"



#============================== Client abstraction -----------

def main():

	p1 = Person("Tarlan", "Omarbayli")
	p2 = Person("Aydan", "Sheydayeva")
	p3 = Person("Famil", "Babayev")

	bus = Bus("123")

	for person in (p1, p2, p3):
		person.get_on_bus(bus)


	bus.remove_person("Aydan", "Sheydayeva")
	bus.move(4.6, 7.7)
	bus.remove_person("Tarlan", "Omarbayli")
	bus.move(5.5, 7.7)
	bus.remove_person("Famil", "Babayev")

	for person in (p1, p2, p3):
		print(f"{person.name} in {person.coordinates}")


if __name__ == "__main__":
	main()



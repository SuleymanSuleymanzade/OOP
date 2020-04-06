import abc

class Pizza(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def get_price(self):
		pass

	@abc.abstractmethod
	def get_status(self):
		pass


class Pepperoni(Pizza):
	__pizza_price = 1.0

	def get_price(self):
		return self.__pizza_price
	
	def get_status(self):
		return "Pepperoni"


class Supreme(Pizza):
	__pizza_price = 1.5

	def get_price(self):
		return self.__pizza_price
	
	def get_status(self):
		return "Supreme"


class PizzaDecorator(Pizza):
	def __init__(self, pizza):
		self.pizza = pizza

	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()



class Tomato(PizzaDecorator):
	def __init__(self, pizza):
		super(Tomato, self).__init__(pizza)
		self.__tomato_price = 2.0

	@property
	def price(self):
		return self.__tomato_price

	def get_price(self):
		return super(Tomato, self).get_price() + self.__tomato_price 

	def get_status(self):
		return super(Tomato, self).get_status() + " Tomato"


class Cheese(PizzaDecorator):
	def __init__(self, pizza):
		super(Cheese, self).__init__(pizza)
		self.__cheese_price = 1.5

	@property
	def price(self):
		return self.__cheese_price

	def get_price(self):
		return super(Cheese, self).get_price() + self.__cheese_price

	def get_status(self):
		return super(Cheese, self).get_status() + " Cheese"


#=========================Buisnes Layer ===================================================

class PizzaBuilder:
	def __init__(self, pizza_type):
		self.pizza_type = pizza_type
		self.pizza = eval(pizza_type)()
		
	def add_extention(self, extention):
		'''
		if extention == "tomato":
			self.pizza = Tomato(self.pizza)
		elif extention == "cheese":
			self.pizza = Cheese(self.pizza)
		'''
		self.pizza = eval(extention)(self.pizza)
		self.extentions_list.append(extention)

	def remove_extention(self, extention):
		
		if extention in self.extentions_list:
			self.extentions_list.remove(extention)
		
		temp_pizza = eval(self.pizza_type)()
		for ex in self.extentions_list:
			temp_pizza = eval(ex)(temp_pizza)
		
		self.pizza = temp_pizza


	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()


#===================== Client part (object abstraction) ======================
'''
my_pizza =  Tomato(Cheese(Tomato(ConcretePizza())))

print(my_pizza.get_price())
print(my_pizza.get_status())
'''

pizza = PizzaBuilder('Pepperoni')

pizza.add_extention('Tomato')
pizza.add_extention('Cheese')
pizza.add_extention('Tomato')

print(pizza.get_status())
print(pizza.get_price())

pizza.remove_extention('Cheese')
print('------------------------------------')

print(pizza.get_price())

print('---------------------------------------')

pizza.add_extention('Tomato')
print(pizza.get_price())
print(pizza.get_status())

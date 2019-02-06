class Person(object):

	# constructor, called automatically when the object
	# is created; invoked by python which also supplies a
	# a reference of the newly constructed object
	def __init__(self, name=None, city='Bangalore'):
		# print('Person instance created')
		self.__name = name
		self.__city = city

	def info(self):
		print('Name =', self.__name)
		print('City =', self.__city)
		print('-'*50)

def main():
	p1 = Person(name='Vinod', city='Bangalore')
	p2 = Person(name='Shyam', city='Shivamogga')
	p3 = Person('Ramesh')
	
	p1.info()
	p2.info()
	p3.info()

if __name__ == '__main__':
	main()
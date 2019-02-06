# ex10.py

class Person:
	# this is equivalent of 'static methods' in Java/C#
	def hello():
		print('Hello, world!')

	# this is equivalent of 'non-static/object method' in Java/C#
	# all object methods must have the first parameter to represent
	# the invoking object, usually named as 'self'
	def info(self, n):
		print('Person information here...')
		print('id of self is', id(self))
		print('n is', n)

		# adding a new member data to the 'self'
		self.name = 'Vinod'
		self.city = 'Bangalore'


def main():
	p1 = Person()
	print('type of p1 is', type(p1))
	print('id of p1 is', id(p1))

	print(dir(p1))
	p1.info(100)
	print(dir(p1))

	
	Person.hello()
	# Person.info(p1, 123)
	# print(p1)


if __name__ == '__main__':
	main()




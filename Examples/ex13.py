# ex13.py
from ex12 import Employee

class Contractor(object):
	def __init__(self, **kwargs):
		print('Contractor.__init__ called')

	def test(self):
		print('Contractor.test() called')

	def info(self):
		print('Contractor.info() called')

class Salesman(Contractor, Employee):

	def __init__(self, **kwargs):
		# super().__init__(**kwargs)
		print('Salesman.__init__ called')
		Employee.__init__(self, **kwargs)
		Contractor.__init__(self, **kwargs)
		self.__target = kwargs.get('target', 100000)

	def info(self):
		# super().info()
		Employee.info(self)
		print('Target  : {}'.format(self.__target))
		print('-' * 50)


def main():
	s1 = Salesman(name='Ravi', id=12, target=150000)
	s1 += 200
	s1 += ' Kumar'

	print(s1)
	s1.info()

if __name__ == '__main__':
	main()
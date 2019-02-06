class Employee(object):

	def __init__(self, **kwargs):
		print('Emplyee.__init__ called')
		self.__id = kwargs.get('id')
		self.__name = kwargs.get('name')
		self.__salary = kwargs.get('salary', 1500)
		self.__dept = kwargs.get('dept', 'SALES')

	def info(self):
		print('Id      : {}'.format(self.__id))
		print('Name    : {}'.format(self.__name))
		print('Salary  : $ {}'.format(self.__salary))
		print('Dept    : {}'.format(self.__dept))

	def set_name(self, name):
		self.__name = name

	# getter/setter for property 'id'
	@property
	def id(self):
		return self.__id
	@id.setter
	def id(self, id):
		self.__id = id

	# getter/setter for property 'name'
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self, name):
		self.__name = name

	# getter/setter for property 'salary'
	@property
	def salary(self):
		return self.__salary
	@salary.setter
	def salary(self, salary):
		self.__salary = salary

	# getter/setter for property 'dept'
	@property
	def dept(self):
		return self.__dept
	@dept.setter
	def dept(self, dept):
		self.__dept = dept

	def __str__(self):
		return 'Employe (id={}, name={}, salary={}, dept={})'.format(
			self.__id, self.__name, self.__salary, self.__dept)
	
	def __lt__(self, obj):
		if type(obj) not in [Employee]:
			raise TypeError('RHS must be an Employee instance')
		return self.__id < obj.__id	

	def __iadd__(self, obj): 
		if type(obj) in [int, float]:
			self.__salary += obj
		elif type(obj) in [str]:
			self.__name += obj
		else:
			raise TypeError('RHS must be one of str, int, float')

		return self

def main():
	e1 = Employee(name='John', id=1122, salary=2400)
	e2 = Employee(name='Jane', id=2233, dept='ADMIN')
	e3 = Employee(name='Smith', id=2345)
	e4 = Employee()

	e1 += 500
	e1 += ' Miller'

	# e4.__name = 'Martin' # does not change the member __name
	# e4.set_name('Martin')
	e4.name = 'Martin' # should invoke a 'setter' method
	e4.salary = 2200
	e4.id = 7788
	e4.dept = 'PRODUCTION'
	# print(e4.name) # should invoke a 'getter' method

	# e1.salary = e1.salary + 500
	# e1.name = e1.name + ' Miller'

	emps = [e1, e2, e3, e4]
	# for e in sorted(emps, key=lambda e:e.id): print(e)
	for e in sorted(emps): print(e)



if __name__ == '__main__':
	main()








# ex08.py

def print_report(title, username='guest', *args, **kwargs):
	print('title =', title)
	print('username =', username)
	print('args =', args)
	print('kwargs =', kwargs)
	line()

def main():
	print_report('Monthly report')
	print_report('Monthly report', 'vinod')
	print_report(username='john', title='Yearly report')
	print_report('Monthly report', 'ramesh', 100, 200)
	print_report('Monthly report', 'ramesh', 100, 200, x=20, y=50)


def create_person(**kwargs):
	p = dict()
	p['name'] = kwargs.get('name')
	p['city'] = kwargs.get('city', 'Bangalore')
	p['email'] = kwargs.get('email')
	return p

def main_3():
	p1 = create_person(name='Vinod', email='vinod@vinod.co')
	p2 = create_person(name='Ramesh')
	p3 = create_person(city='Chennai', name='Sujay', email='sujay@example.com')

	print(p1)
	print(p2)
	print(p3)

def calc_sum(*args):
	# print('type of args is', type(args))
	# print('args is', args)
	args = [a for a in args if type(a) in (int, float)]
	return sum(args)

def main_2():
	s = calc_sum(12, 30, 'vinod', 50)
	print('sum = ', s)
	s = calc_sum(1, 2, 4, 5, 'x', 'y', 7, 4, 4, 56, 7, 88, 5)
	print('sum = ', s)

def print_data(name, city=None, email=None):
	print('name  =', name)
	print('city  =', city)
	print('email =', email)
	line()

def line():
	print('-'*50)

def main_1():
	print_data('vinod', 'bangalore', 'vinod@vinod.co')

	input1 = ['john', 'dallas', 'john@example.com']
	print_data(*input1)

	input2 = ('john', 'dallas', 'john@example.com')
	print_data(*input2)

	# set does not guarantee the order of items
	# so, do not use like this:
	input3 = {'jane', 'chicago'}
	print_data(*input3)

	print_data(name='rahul', email='rahul@exmaple.com')

	input4 = {'name': 'ravi', 'city': 'mysore'}
	print_data(**input4)

if __name__ == '__main__':
	main()








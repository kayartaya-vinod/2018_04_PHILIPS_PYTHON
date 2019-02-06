# ex03.py

# The default value for a parameter is assigned
# only once during the loading of the module
def max_days(month = 1, year = 2018):
	if type(month) != int : raise Exception('Month must be integer')
	if type(year) != int : raise Exception('Year must be integer')

	if month==2:
		if is_leap(year):
			return 29
		else:
			return 28
	elif month in [4, 6, 9, 11]:
		return 30
	elif month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	else:
		raise Exception('Invalid month. Must be between 1 to 12')


def is_leap(year):
	'''This is a function to check if the input
	is a leap year or not. A leap year occurs once 
	in 4 years and not in every 100 years and occurs again
	once in 400 years.

	This is created by Vinod <vinod@vinod.co> for Philips.
	'''

	if type(year) != int:
		print('Input was not a number: ', year)
		return

	if year%400==0 or (year%4==0 and year%100!=0):
		return True
	else:
		return False


if __name__ == '__main__':
	# execute this part only if this module is executed directly
	# and not via an 'import' statement

	yr = input('Enter a year: ')
	yr = int(yr)

	if is_leap(yr):
		print('Input is a leap year')
	else:
		print('Input is not a leap year')











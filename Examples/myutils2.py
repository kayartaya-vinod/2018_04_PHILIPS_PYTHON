# myutils.py

# some useful methods

def num2words(number=0):
	if type(number)!=int: raise Exception('Input must be a number!')
	if number>999999999999: raise Exception('Input must be <=999999999999')

	nums = '{:,}'.format(number).split(',')

	lst = ',thousand,million,billion,trillion'.split(',')
	i = len(nums) -1
	result = ''
	while len(nums)>0:
		n = int(nums.pop(0))
		if n>0: 
			word = __num2words3digits__(n) + ' ' + lst[i]
			result += word + ' '
		i -= 1

	return result

def __num2words3digits__(num):
	a, b = num//100, num%100

	result = ''
	if a!=0:
		result += __num2words__(a) 
		result += " hundred "

	result += __num2words__(b)
	return result

def __num2words__(num):
	'''This function receives a two digit number and returns the 
	string equivalant of the same'''

	l1 = ',one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')

	l2 = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')

	if num<20:
		return l1[num]
	else:
		a, b = num//10, num%10
		return l2[a] + ' ' + l1[b]

def main():
	words = num2words(223456789456)
	print(words)


if __name__ == '__main__':
	main()


# myutils.py

# some useful methods

def num2words(number=0):
	if type(number)!=int: raise Exception('Input must be a number!')
	if number>999999999: raise Exception('Input must be <=999999999')

	# convert the input into a stack of two digit numbers
	nums = []
	i = 1
	while number>0:
		if i==2:
			nums.append(number%10)
			number //= 10
		else:
			nums.append(number%100)
			number //= 100
		i += 1

	lst = ',hundred,thousand,lakh,crore'.split(',')
	i = len(nums) -1
	result = ''
	while len(nums)>0:
		n = nums.pop()
		if n>0: 
			word = __num2words__(n) + ' ' + lst[i]
			result += word + ' '
		i -= 1

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
	words = num2words(120056000)
	print(words)


if __name__ == '__main__':
	main()


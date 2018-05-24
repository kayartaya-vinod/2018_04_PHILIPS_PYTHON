# ex02.py

# script to accept two numbers and print the largest of them

num1 = input('Enter a number: ')
num2 = input('Enter aother number: ')

num1 = int(num1)
num2 = int(num2)

if num1>num2:
	big = num1
else:
	big = num2


# print('Biggest of two input is: ', big)
# print('Biggest of %d and %d is %d' % (num1, num2, big))

msg = 'Biggest of {} and {} is {}'.format(num1, num2, big)

print(msg)








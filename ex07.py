# ex07.py

def main():
	total = 0
	while True:
		n = input('Enter a number (0 to stop): ')
		try:
			n = float(n)
			if n==0: break
			total += n
		except ValueError:
			print('Invalid input. Please enter a number')
			# break, return, exit() can be tried here
		except Exception:
			print('Something went wrong!')
		finally:
			print('FINALLY: This executes almost all times!')

		print('This also executes almost all times!')


	print('Total of all inputs = ', total)

if __name__ == '__main__':
	main()

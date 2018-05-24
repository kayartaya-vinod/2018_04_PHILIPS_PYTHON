# ex05.py
import json

def main():
	'''Convert a CSV file into a JSON file'''
	csv_filename = input('Enter CSV filename: ')
	with open(csv_filename) as csf:
		fieldnames = csf.readline().rstrip().split(',')
		temp = [ dict(zip(fieldnames, line.rstrip().split(','))) for line in csf]
		
		json_filename = input('Enter JSON filename: ')
		with open(json_filename, 'w') as jsf: json.dump(temp, jsf, indent=4)

	print('CSV saved as JSON file: ', json_filename)



def main_4():
	json_filename = input('Enter JSON filename: ')

	with open(json_filename) as jsf:
		lst = json.load(jsf)
		keys = lst[0].keys()		
		header = '{},{},{},{}\n'.format(*keys)
		lines = ['{id},{name},{email},{phone}\n'.format(**p) for p in lst]
		lines.insert(0, header)

		csv_filename = input('Enter CSV filename: ')
		with open(csv_filename, 'w') as csf:
			csf.writelines(lines)

	print('JSON file saved in CSV format with filename: ', csv_filename)




def main_3():
	fields = ('title', 'name', 'city')
	with open('data.csv', mode='a+') as file:

		file_size = file.tell()
		lines = []
		if file_size == 0: lines.append(','.join(fields) + '\n')

		ans = 'yes'
		while ans == 'yes':
			title = input('Enter title (Mr./Ms.): ')
			name = input('Enter name: ')
			city = input('Enter city: ')
			lines.append(','.join([title, name, city]) + '\n')

			ans = input('Wish to add another? yes/no: ')

		file.writelines(lines)

def main_2():
	filename = input('Enter filename: ')
	with open(filename) as file:
		for line in file:
			print(line, end='')

def main_1():
	filename = input('Enter filename: ')
	file = open(filename)

	ln = 1
	for line in file.readlines():
		print('{}. {}'.format(ln, line), end='')
		ln += 1

	file.close()


if __name__ == '__main__':
	main()
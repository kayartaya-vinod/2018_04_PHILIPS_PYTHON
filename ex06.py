import requests

url = 'http://kelutral.com/rest/contacts.php'

def add_new_contact(c1):
	if type(c1) != dict: raise ValueError('Dictionary was required')

	resp = requests.post(url, json=c1)
	d = resp.json()
	if d['success'] == False:
		print('Could not add the data: Reason {message}'.format(**d))
	else:
		print('Added data with id: {id}'.format(**d))
		get_contact_by_id(d['id'])

def get_contact_by_id(id):
	params = {'id': id}
	d = {'http': 'http://165.225.96.34:9480'}

	resp = requests.get(url, params) #, proxies = d)
	c1 = resp.json()

	# print(c1)

	print('Name = {first_name} {last_name}'.format(**c1))
	print('City = {city}'.format(**c1))


def main():
	# get_contact_by_id(1)
	p1 = dict(first_name='Kishore', last_name='Kumar')
	p1['city'] = 'Delhi'

	add_new_contact(p1)


if __name__ == '__main__':
	main()
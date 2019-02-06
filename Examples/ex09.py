# ex09.py

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

people = []
people.append(dict(id=1, name='rahul', age=22, city='bangalore'))
people.append(dict(id=2, name='rajesh', age=34, city='bangalore'))
people.append(dict(id=3, name='mahesh', age=14, city='mysore'))
people.append(dict(id=4, name='ajay', age=55, city='tumkur'))

@app.route('/api/contacts/', methods=['GET'])
def get_all():
	return jsonify({'success': True, 'data': people})

@app.route('/api/contacts/<int:id>')
def get_one(id):
	p = [p for p in people if id==p['id']]
	if len(p)==0:
		abort(404)
	return jsonify({'success': True, 'data': p[0]})

@app.route('/api/contacts/', methods=['POST'])
def create_contact():
	if request.json: 
		d = request.json
		if len([p for p in people if p['id']==d['id']]) != 0:
			abort(404)

		people.append(d)
		return jsonify({'success': True, 'data': request.json})
	else:
		abort(404)

@app.errorhandler(404)
def error404_handler(err):
	return make_response(jsonify({'success': False, 
		'message': 'No data found'}), 404)


@app.route('/', methods=['GET', 'POST'])
def home():
	return 'Hello, world!'

if __name__ == '__main__':
	app.run(debug=True, port=1234)



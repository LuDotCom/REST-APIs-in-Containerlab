from flask import Flask, jsonify, request

app = Flask(__name__)

students = { 'AX0001': {'Name': 'Luca', 'Surname': 'Com', 'Birth_Year': 1996} }

@app.route('/students')
def get_students():
	return jsonify(students)
	
@app.route('/students', methods=['POST'])
def add_students():
	students.update(request.get_json())
	return '', 204
	

if __name__ == '__main__':
	app.run(host="192.168.1.21", port=5000)

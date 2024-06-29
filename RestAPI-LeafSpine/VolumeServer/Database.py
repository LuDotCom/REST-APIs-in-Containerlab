from flask import Flask, jsonify, request, abort
import os
import json

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def add_students():
    data = request.get_json()
    if not data:
        abort(400, 'Invalid JSON data')
    
    for student_id, student_info in data.items():
        with open(f'{student_id}.json', 'w') as f:
            json.dump({student_id: student_info}, f)
    
    return '', 204

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    file_path = f'{student_id}.json'
    
    if not os.path.exists(file_path):
        abort(404, 'Student ID not found')
    
    with open(file_path, 'r') as f:
        student_data = json.load(f)
    
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(host="192.168.1.41", port=5000)


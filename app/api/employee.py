from flask import request, jsonify

from app import app
from app.objects.employee import Employee


@app.route('/api/employees', methods=['POST'])
def employees():
    if request.method == 'POST':
        new_emp = Employee(**request.form)
        return jsonify(new_emp.create())
    return jsonify({'complete': False})

@app.route('/api/employees/<int:emp_id>', methods=['PUT', 'DELETE'])
def employee(emp_id):
    if request.method == 'PUT':
        emp = Employee(id=emp_id, **request.form)
        return jsonify(emp.update())

    elif request.method == 'DELETE':
        emp = Employee(id=emp_id)
        return jsonify(emp.delete())

    return jsonify({'complete': False})
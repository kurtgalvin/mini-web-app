from flask import request, jsonify

from app import app
from app.objects.employee import Employee


@app.route('/api/employee', methods=['POST'])
def employee():
    if request.method == 'POST':
        new_emp = Employee(**request.form)
        return jsonify(new_emp.create())
    return jsonify({'complete': False})
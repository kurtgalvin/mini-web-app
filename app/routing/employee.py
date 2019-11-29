from flask import render_template, redirect

from app import app
from app.objects.employee import Employee


@app.route('/employees/<int:emp_id>')
def employee_index(emp_id):
    try:
        emp = Employee(id=emp_id)
    except TypeError:
        return redirect('/')
    context = {
        'form_fields': Employee.form_fields(),
        'employee': emp.__dict__
    }
    return render_template('employee.html', **context)
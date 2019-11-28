from flask import render_template, request

from app import app
from app.objects.employee import Employee


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.environ['REQUEST_METHOD'] == 'POST':
        new_emp = Employee(**request.form)
        new_emp.create()

    context = {
        'form_fields': Employee.form_fields()
    }
    return render_template('index.html', **context)
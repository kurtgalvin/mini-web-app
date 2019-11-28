from flask import render_template

from app import app
from app.objects.employee import Employee


@app.route('/')
def index():
    context = {
        'form_fields': Employee.form_fields(),
        'all_employees': Employee.get_all()
    }
    return render_template('index.html', **context)
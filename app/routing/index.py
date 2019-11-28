from flask import render_template

from app import app
from app.objects.employee import Employee


@app.route('/')
def index():
    Employee()
    return render_template('index.html')
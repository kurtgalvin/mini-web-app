from flask import Flask
import os

print(os.environ.get('test'))

app = Flask("app")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from .routing.index import *
from .routing.employee import *
from .api.employee import *
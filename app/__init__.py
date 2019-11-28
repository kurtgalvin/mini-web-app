from flask import Flask

app = Flask("app")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from .routing.index import *
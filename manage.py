import sys
from app import app

args = sys.argv[1:]

if "runserver" in args:
    app.run(host="0.0.0.0", port='5001', debug=True)
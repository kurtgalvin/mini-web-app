import sys
import os
from app import app

args = sys.argv[1:]

if "runserver" in args:
    app.run(
        host="0.0.0.0", 
        port=os.environ.get('PORT', '5001'), 
        debug=bool(os.environ.get('debug', True))
    )
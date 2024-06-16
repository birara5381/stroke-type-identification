import sys
import os

# Assuming your Flask app is in a directory called 'stroke-type-identification'
# and the main application file is 'app.py' with the Flask instance named 'app'

sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

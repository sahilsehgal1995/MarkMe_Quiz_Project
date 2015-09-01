#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/sahil/my/'New Folder'/prog/python/flask/quiz/")

from FlaskApp import app as application
application.secret_key = 'HARD TO GUESS.'

from flask import Flask

app = Flask(__name__) #init the flask app

#import all views/routes
from main import routes

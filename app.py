from flask import Flask

app = Flask(__name__) #init the flask app

#import all views
from views.routes import *

if __name__ == '__main__': #condition to run the app
    app.run(debug=True)

# imports the Flask class from flask.py,
# which was installed by venv/ and 'pip install Flask'
from flask import Flask 

# instantiates the Flask application
# _name_ = _main_ if 'python app.py' is run in terminal
app = Flask(__name__)
# activates Flask's debug functionality
app.debug = True

# declares new Route for application,
# in this case it is root ('/') of the app and only GET requests allowed
@app.route('/', methods=['GET'])

# sets up function to be executed when user visits 'root' route
def hello():
	return "Hello, world!"

if __name__ == "__main__":
	app.run(host="127.0.0.1")

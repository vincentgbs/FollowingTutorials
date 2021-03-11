from flask import Flask


app = Flash(__name__)
app.config['SECRET_KEY'] = 'random_string'

# import routes AFTER instantiating app
from routes import *

if __name__ == '__main__':
    app.run(debug=True)

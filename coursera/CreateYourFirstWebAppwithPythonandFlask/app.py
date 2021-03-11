from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flash(__name__)
app.config['SECRET_KEY'] = 'random_string'
ap.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)dels.property

# import routes AFTER instantiating app
from routes import *

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Base de données
db = SQLAlchemy(app)

from app import routes, models

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

USER = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'restaurante_db'

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

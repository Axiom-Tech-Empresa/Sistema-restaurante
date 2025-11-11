from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from main import app

USER = 'root'
PASSWORD = '1234'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'restaurante_db'

# Constrói a URI de conexão
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def uri():
    return app.config['SQLALCHEMY_DATABASE_URI']
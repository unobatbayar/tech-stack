from flask import Flask
from flask_sqlalchemy import SQLAlchemy

host = '127.0.0.1:5000'
user = 'root'
password = 'new_password'
database = 'ORMDB'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255), nullable=False)

db.create_all()    
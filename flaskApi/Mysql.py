from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine


app =  Flask(__name__)
#"mysql://username:password@localhost/db_name"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/users_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect to the database
engine = create_engine("mysql+mysqlconnector://root:root@localhost/users_python")

# Test the connection
connection = engine.connect()
# result = connection.execute("SELECT * FROM users_python.Players")
# print(result)

# db = SQLAlchemy(app) #instantiation

# class User(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(80), unique=True)
#     def __init__(self, username, email):
#         self.username = username
#         self.email =  email
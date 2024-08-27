from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


app =  Flask(__name__)
#"mysql://username:password@localhost/db_name"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/users_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app) #instantiation

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    def __init__(self, username, email):
        self.username = username
        self.email =  email
    




items = [
    {
        "name": "Pizza",
        "Price": "160"
    },
    {
        "name": "Dimsum",
        "Price": "80"
    }
]

@app.route('/get_items')
def get_items():
    return items

@app.get('/get_item/<string:name>')
def get_item(name):
    for i in items:
        if name == i['name']:
            return i
    return {'message': "Record Does not exist"}

@app.post('/add_item')
def add_item():
    request_data = request.get_json()
    print(request_data)
    items.append(request_data)
    return "Item added successfully", 201


@app.route('/')
def hello():
    return "Hello, user"


if __name__ == '__main__':
    app.run()
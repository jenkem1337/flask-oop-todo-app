from flask_todo_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    todo = db.relationship('Todo', backref='user')

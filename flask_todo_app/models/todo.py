from flask_todo_app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    todoText = db.Column(db.String(255), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    isComplete = db.Column(db.Boolean, default=False)


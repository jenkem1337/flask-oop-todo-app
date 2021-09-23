
from flask_todo_app.models.todo import Todo
from flask_todo_app import db
from flask_todo_app.dao.abstract.todoDao import ITodoDao

class TodoDao(ITodoDao):

    def createTodo(self,todoText, userID):
        todo = Todo()
        todo.todoText = todoText
        todo.userID = userID
        db.session.add(todo)
        db.session.commit()
    
    def removeTodo(self,id):
        todo = Todo.query.get(id)  
        db.session.delete(todo)
        db.session.commit()

    def updateTodo(self,id, todoText):
        todo = Todo.query.get(id)
        todo.todoText = todoText
        db.session.commit()

    def getAllTodos(self,userID):
        todo = Todo.query.filter_by(userID = userID).all()
        return todo

    def findById(self,id):
        todo = Todo.query.get(id)
        return todo
    
    def toggleTodo(self, id):
        todo = Todo.query.get(id)
        todo.isComplete = not todo.isComplete
        db.session.commit()
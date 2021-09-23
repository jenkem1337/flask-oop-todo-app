from flask_todo_app.dao.abstract.todoDao import ITodoDao
from flask_todo_app.services.abstract.todoService import ITodoService


class TodoService(ITodoService):
    def __init__(self, todoDao: ITodoDao):
        self.__todoDao = todoDao
    
    def createTodo(self, todoText, userID):
        self.__todoDao.createTodo(todoText, userID)
    
    def removeTodo(self,id):
        self.__todoDao.removeTodo(id)
    
    def updateTodo(self, id, todoText):
        self.__todoDao.updateTodo(id,todoText)

    def findById(self,id):
        return self.__todoDao.findById(id)

    def getAllTodos(self, userID):
        return self.__todoDao.getAllTodos(userID)
    
    def toggleTodo(self, id):
        self.__todoDao.toggleTodo(id)
    
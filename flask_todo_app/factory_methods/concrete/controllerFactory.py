from flask_todo_app.factory_methods.abstract.controllerFactory import IControllerFactory
from flask_todo_app.controllers.userController import UserController
from flask_todo_app.controllers.todoController import TodoController
from flask_todo_app.dao.concrete.userDao import UserDao
from flask_todo_app.dao.concrete.todoDao import TodoDao 
from flask_todo_app.services.concrete.todoService import TodoService
from flask_todo_app.services.concrete.userService import UserService


class ControllerFactory(IControllerFactory):
    
    @staticmethod
    def createController(string):
        if   string == 'USER_CONTROLLER':
            return UserController(UserService(UserDao()))
        elif string == 'TODO_CONTROLLER':
            return TodoController(TodoService(TodoDao()))
        else:
            return 'hatalı değer'
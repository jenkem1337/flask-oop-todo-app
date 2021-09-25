from flask_todo_app.services.abstract.userService import IUserService
from flask_todo_app.dao.abstract.userDao import IUserDao
from flask_todo_app.services.abstract.userService import IUserService

class UserService(IUserService):
    def __init__(self, userDao: IUserDao):
        self.__userDao = userDao
    
    def createUser(self, username, password, email):
        self.__userDao.createUser(username,password,email)
    
    def getUserForLogin(self, username,password):
        return self.__userDao.getUserForLogin(username, password)

    def updateUserDetail(self, id, username, password, email):
        self.__userDao.updateUserDetail(id,username,password,email)

    def findByUsername(self,username):
        return self.__userDao.findByUsername(username)

    def findById(self,id):
        return self.__userDao.findById(id)
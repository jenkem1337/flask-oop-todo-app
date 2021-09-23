from flask_todo_app import db
from flask_todo_app.models.user import User
from flask_todo_app.dao.abstract.userDao import IUserDao


class UserDao(IUserDao):
        
        def createUser(self,username, password, email):
                user = User()
                user.username = username
                user.password = password
                user.email = email
                db.session.add(user)
                db.session.commit()
    
        def getUser(self,username, password):
                user = User.query.filter_by(username = username, password = password).first()
                return user
        
        def findByUsername(self,username):
                user = User.query.filter_by(username=username).first()
                return user

        def findById(self, id):
                user = User.query.get(id)
                return user

        def updateUserDetail(self, id, username, password, email):
                user = User.query.get(id)
                user.username = username
                user.password = password
                user.email = email
                db.session.commit()
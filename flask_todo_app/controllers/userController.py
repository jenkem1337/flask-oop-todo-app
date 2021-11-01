from flask_todo_app.services.abstract.userService import IUserService
from flask import render_template, url_for, request, redirect, session


class UserController:

    def __init__(self, userservice: IUserService):
        self.__userService = userservice
    
    def createUser(self):
        if request.method == 'POST':
            error = None
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            
            user = self.__userService.findByUsername(username)
            if user:
                error = 'This user already exist'
                return render_template('register.html', error=error)

            self.__userService.createUser(username, password, email)
            return redirect(url_for('login'))
        
        if request.method == 'GET':
            return render_template('register.html')

    def getUserForLogin(self):
        if request.method =='POST':
            error = None
            username = request.form['username']
            password = request.form['pass']
            user = self.__userService.getUserForLogin(username, password)
            
            if not user:
                error = 'This person does not exist'
                return render_template('login.html', error = error)

            session['userID'] = user.id
            session['username'] = user.username
            return redirect(url_for('index'))
        
        if request.method == 'GET':
            return render_template('login.html')

    def updateUserDetail(self, id):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['pass']
            email = request.form['email']

            session['username'] = username
            self.__userService.updateUserDetail(id,username, password, email)
            return redirect(url_for('todos'))
        
        if request.method=='GET':
            user = self.__userService.findById(id)
            
            if session['userID'] != id:
                return render_template('error-page.html')
            
            userName = user.username
            userPass = user.password
            userEmail = user.email
            return render_template('update-user.html', userName = userName, userPass = userPass, userEmail = userEmail)
        
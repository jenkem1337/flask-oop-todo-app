from flask_todo_app import app
from flask import session, redirect, url_for, render_template
from flask_todo_app.decorators import login_required
from flask_todo_app.factory_methods.concrete.controllerFactory import ControllerFactory


userController = ControllerFactory.createController('USER_CONTROLLER')
todoController = ControllerFactory.createController('TODO_CONTROLLER')

@app.route('/', methods=['GET','POST'])
def index():
    if session.get('username'):
        username = session['username']
        return render_template('index.html', username = username)
    
    return render_template('index.html')
@app.route('/register' ,methods=['GET','POST'])
def register():
    return userController.createUser()


@app.route('/login', methods=['GET','POST'])
def login():
    return userController.getUserForLogin()

@app.route('/updateUser/<int:id>', methods=['GET','POST'])
@login_required
def updateUser(id):
    return userController.updateUserDetail(id)

@app.route('/todos', methods=['GET','POST'])
@login_required
def todos():
    return todoController.listAllTodosAndCreateTodo()

@app.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    return todoController.updateTodo(id)


@app.route('/delete/<int:id>', methods=['GET','POST'])
@login_required
def deleteTodo(id):
    return todoController.deleteTodo(id)

@app.route('/toggleTodo/<int:id>',methods=['GET','POST'])
@login_required
def toggleTodo(id):
    return todoController.toggleTodo(id)


@app.route('/logout', methods =['GET','POST'])
@login_required
def logout():
    session.pop('username',None)
    session.pop('userID',None)
    return redirect(url_for('index'))

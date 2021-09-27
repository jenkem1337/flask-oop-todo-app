from flask_todo_app.services.abstract.todoService import ITodoService
from flask import render_template, url_for, request, redirect, session

class TodoController:
    
    def __init__(self,todoservice: ITodoService):
        self.__todoService = todoservice
    
    def listAllTodosAndCreateTodo(self):
        if request.method =='POST':
            id = session['userID']
            newTodo = request.form['todo']
                        
            self.__todoService.createTodo(newTodo, id)
            return redirect(url_for('todos'))
        
        if request.method == 'GET':
            id = session['userID']
            username = session['username']
            todos = self.__todoService.getAllTodos(id)
            return render_template('list.html',todos = todos, username = username, userID = id)

    def updateTodo(self, id):
        if request.method =='POST':
            newTodo = request.form['new_todo']
            
            self.__todoService.updateTodo(id, newTodo)
            return redirect(url_for('todos'))
        
        if request.method == 'GET':
            oldTodo = self.__todoService.findById(id)
            oldTodo = oldTodo.todoText
            return render_template('update.html', oldTodo = oldTodo)
        

    def toggleTodo(self,id):
        if request.method =='GET':
            self.__todoService.toggleTodo(id)
            return redirect(url_for('todos'))

    def deleteTodo(self, id):
        if request.method == 'GET':
            self.__todoService.removeTodo(id)
            return redirect(url_for('todos'))

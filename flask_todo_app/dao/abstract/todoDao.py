from abc import ABC, abstractmethod

class ITodoDao(ABC):
    @abstractmethod
    def createTodo(self,todoText, userID):
        pass
    
    @abstractmethod
    def removeTodo(self,id):
        pass
    
    @abstractmethod
    def updateTodo(self,id, todoText):
        pass
    
    @abstractmethod
    def getAllTodos(self,userID):
        pass
    
    @abstractmethod
    def findById(self,id):
        pass
    
    @abstractmethod
    def toggleTodo(self,id):
        pass
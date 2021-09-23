from abc import ABC, abstractmethod

class ITodoService(ABC):

    @abstractmethod
    def createTodo(self, todoText, userID):
        pass
    @abstractmethod
    def removeTodo(self,id):
        pass
    @abstractmethod
    def updateTodo(self, id, todoText):
        pass
    @abstractmethod
    def findById(self,id):
        pass
    @abstractmethod
    def getAllTodos(self, userID):
        pass
    @abstractmethod
    def toggleTodo(self,id):
        pass
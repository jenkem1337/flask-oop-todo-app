from abc import ABC, abstractmethod

class IUserService(ABC):

    @abstractmethod
    def createUser(self, username, password, email):
        pass

    @abstractmethod
    def getUser(self, username,password):
        pass

    @abstractmethod
    def updateUserDetail(self, id, username, password, email):
        pass

    @abstractmethod
    def findByUsername(self,username):
        pass

    @abstractmethod
    def findById(self,id):
        pass
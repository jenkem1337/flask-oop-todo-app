from abc import ABC, abstractmethod

class IControllerFactory(ABC):

    @staticmethod
    @abstractmethod
    def createController(string):
        pass
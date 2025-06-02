from abc import ABC,abstractmethod
class RBIApp(ABC):
    @abstractmethod
    def depositAmount(self):
        pass
    @abstractmethod
    def withdrawAmount(self):
        pass
    @abstractmethod
    def checkBalance(self):
        pass
    def openFDAccount(self):
        pass
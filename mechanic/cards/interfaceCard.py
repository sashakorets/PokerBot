from abc import abstractmethod, ABC

class interfaceCard(ABC):
    @abstractmethod
    def setCard(self):
        pass

    @abstractmethod
    def getCard(self):
       pass
from abc import abstractmethod
class gameRound:

    @abstractmethod
    def setCurrentlyPos(self, flag):
        pass

    @abstractmethod
    def getCurrentlyPos(self):
        pass

    @abstractmethod
    def move(self, tgID, action):
        pass
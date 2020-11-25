from mechanic.cards.hand import Hand

class Player:
    def __init__(self, tgID, stack: int, fold: bool, position: bool, bet: int):
        self.__ID = tgID
        self.__hand = Hand()
        self.__stack = stack
        self.__fold = fold
        self.__position = position
        self.__bet = bet

    def getID(self):
        return self.__ID

    def setPos(self, flag):
        if flag:
            self.__position = True
        else:
            self.__position = False

    def getPos(self):
        return self.__position

    def setStack(self, val: int):
        if val != 0:
            self.__stack += val
        else:
            return

    def getStack(self):
        return self.__stack

    def setHand(self, deck, flag: bool):
        self.__hand.setHand(deck, flag)

    def getHand(self):
        return self.__hand.getHand()

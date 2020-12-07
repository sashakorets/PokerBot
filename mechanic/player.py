from treys import Card
from mechanic.cards.hand import Hand

class Player:
    def __init__(self, tgID, tgFname, stack: int, fold: bool, position: bool, bet: int):
        self.__ID = tgID
        self.__Fname = tgFname
        self.__hand = Hand()
        self.__stack = stack
        self.__fold = fold
        self.__position = position
        self.__bet = bet

    def getID(self):
        return self.__ID

    def getFname(self):
        return self.__Fname

    def setFold(self, flag):
        if flag:
            self.__fold = True
        else:
            self.__fold = False
    def getFold(self):
        return self.__fold

    def setPos(self, flag):
        if flag:
            self.__position = True
        else:
            self.__position = False
    def getPos(self):
        return self.__position

    def setStack(self, val: int):
        self.__stack += val
    def getStack(self):
        return self.__stack

    def setBet(self, val: int):
        self.__bet += val
    def getBet(self):
        return self.__bet

    def setHand(self, deck, flag: bool):
        self.__hand.setCard(deck, flag)
    def getHand(self, var: str):
        if var == 'lca':
            if not isinstance(self.__hand.getCard(), str):
                return Card.print_pretty_cards(self.__hand.getCard())
        elif var == 'lin':
            return self.__hand.getCard()
        else:
            print('no correct flag')
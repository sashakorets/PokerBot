from treys import Evaluator, Deck, Card
from mechanic.player import Player
from mechanic.cards.board import Board

class Table:
    def __init__(self):
        self.__players = [x for x in range(9)]
        self.__deck = Deck()
        self.__board = Board()

    def refresh(self):
        # refresh deck
        self.__deck = Deck()
        # set hand/position
        # clean fold/bet in player

    def addPl(self, tgID, stack = 1000, fold = True, position = False, bet = 0):
        for i in range(9):
            if not isinstance(self.__players[i], Player):
                self.__players[i] = Player(tgID, 1000, True, False, 0)
                return
            else:
                continue

    def delPl(self, tgID):
        for i in range(9):
            if isinstance(self.__players[i], Player):
                if self.__players[i].getID() == tgID:
                    self.__players[i] = i
                    return
                else:
                    continue
            else:
                continue

    def getPl(self):
        res = []
        for i in self.__players:
            if isinstance(i, Player):
                res.append([i.getID(), i.getHand(), i.getStack()])
            else:
                res.append(i)
        return res

    def setBoard(self):
        self.__board.setBoard(self.__deck, True)

    def getBoard(self, flag: str):
        return self.__board.getBoard(flag)

    def play(self, tgID, ):
        pass


a = Table()
a.setDeck()
print(a)
a.addPl('12321',123,True,False,0)
a.addPl('qwe',1234,True,False,0)
a.addPl('asd',12345,True,False,0)
a.delPl('qwe')
a.addPl('zxc',1321,True,False,0)
print(a.getPl())
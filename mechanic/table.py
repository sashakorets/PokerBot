from treys import Evaluator, Deck, Card
from mechanic.player import Player
from mechanic.cards.board import Board

class Table:
    def __init__(self, blind=15):
        self.__players = [x for x in range(9)]
        self.__deck = Deck()
        self.__board = Board()
        self.__start = False
        self.__blind = blind
        self.__call = 12
        self.__pot = 0
        self.__currentlyPos = None
        self.__circlestatus = 'river'  #preflop,flop,tern,river

    def getBoSt(self):
        return self.__circlestatus

    def refresh(self):
        # maybe add same other func
        if self.__circlestatus == 'river':
            self.setPot(True)
            self.__deck = Deck()
            self.setAllFoldsAndBets()
            self.setPos()
            self.setCurrentlyPos('fromstaticpos')
            self.setBoard()
            self.setHand(True)
            self.__circlestatus = 'preflop'
        elif self.__circlestatus == 'preflop':
            self.setPot()
            self.setAllFoldsAndBets()
            self.setCurrentlyPos('fromstaticpos')
            self.__circlestatus = 'flop'
        elif self.__circlestatus == 'flop':
            self.setPot()
            self.setAllFoldsAndBets()
            self.setCurrentlyPos('fromstaticpos')
            self.__circlestatus = 'turn'
        elif self.__circlestatus == 'turn':
            self.setPot()
            self.setAllFoldsAndBets()
            self.setCurrentlyPos('fromstaticpos')
            self.__circlestatus = 'river'


    def goplay(self):
        for el in self.__players:
            if isinstance(el, Player):
                if not el.getFold():
                    return False
        else:
            if len(list(filter(lambda x: isinstance(x, Player), self.__players))) >= 2:
                self.refresh()
                return True
            else:
                return False


    def setHand(self, flag):
        for el in self.__players:
            if isinstance(el, Player):
                el.setHand(self.__deck, flag)


    def setAllFoldsAndBets(self):
        for el in self.__players:
            if isinstance(el, Player):
                el.setFold(True)
                el.setBet((-1)*el.getBet())

    def addPl(self, tgID, Fname, stack = 1000, fold = False, position = False, bet = 0):
        for i in range(9):
            if not isinstance(self.__players[i], Player):
                self.__players[i] = Player(tgID, Fname, stack, fold, position, bet)
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

    def getPl(self, flag=''):
        res = []
        if flag == 'test':
            for i in self.__players:
                if isinstance(i, Player):
                    res.append([i.getID(), i.getFname(), i.getHand('lca'), i.getStack(), i.getPos(), i.getFold(), i.getBet()])
                else:
                    res.append(i)
            return res
        elif flag == 'id':
            for i in self.__players:
                if isinstance(i, Player):
                    res.append(i.getID())
            return res
        elif flag == 'fname':
            for i in self.__players:
                if isinstance(i, Player):
                    res.append(i.getFname())
            return res
        elif flag == 'full':
            return self.__players

    def setPot(self, clean = False):
        if not clean:
            for el in self.__players:
                if isinstance(el, Player):
                    self.__pot += el.getBet()
        else:
            self.__pot = 0

    def getPot(self):
        return self.__pot

    def setCurrentlyPos(self, flag):
        temp = 0
        for el in self.__players:
            if isinstance(el, Player):
                if flag == 'fromstaticpos':
                    if el.getPos():
                        self.__currentlyPos = el
                        return
                elif flag == 'next':
                    if temp == 0 and el.getID() == self.__currentlyPos.getID():
                        temp = 1
                    elif temp == 1:
                        self.__currentlyPos = el
                        return
                else:
                    print("set currently pos error")
                    return
        else:
            if temp == 1:
                for i in self.__players:
                    if isinstance(i, Player):
                        self.__currentlyPos = i
                        return

    def setBoard(self):
        self.__board.setCard(self.__deck, True)

    def getBoard(self, flag: str, var: str):
        if var == 'lca':
            if not isinstance(self.__board.getCard(flag), str):
                return Card.print_pretty_cards(self.__board.getCard(flag))
        elif var == 'lin':
            return self.__board.getCard(flag)
        else:
            print('no correct flag')

    # def start(self):
    #     for el in self.__players:
    #         if isinstance(el, Player):
    #             if not el.getFold():
    #                 return False
    #     return True

    def setPos(self):
        flag = 0
        for el in self.__players:
            if isinstance(el, Player):
                if flag == 0:
                    if el.getPos():
                        el.setPos(False)
                        flag = 1
                elif flag == 1:
                    self.setCurrentlyPos('fromstaticpos')
                    el.setPos(True)
                    return
        else:
            for el in self.__players:
                if isinstance(el, Player):
                    if flag == 0:
                        if el.getPos():
                            el.setPos(False)
                            flag = 1
                    elif flag == 1:
                        self.setCurrentlyPos('fromstaticpos')
                        el.setPos(True)
                        return
            else:
                for el in self.__players:
                    if isinstance(el, Player):
                        self.setCurrentlyPos('fromstaticpos')
                        el.setPos(True)
                        return

    def getPos(self):
        # повертає порядковий номер за столом, гравця що повинен ходити
        res = 0
        for el in self.__players:
            if isinstance(el, Player):
                if el.getPos():
                    return res
                else:
                    res += 1

    def getCurrentlyPos(self):
        return self.__currentlyPos


    def payBlind(self):
        flag = 0
        for x in 'qw':    # to do this 2 time
            for i in range(len(self.__players)):
                if isinstance(self.__players[i], Player):
                    if flag == 0:
                        if self.__players[i].getPos():
                            flag = 1
                    elif flag == 1:
                        self.__players[i].setStack(self.__blind*(-1))
                        self.__players[i].setBet(self.__blind)
                        flag = 2
                    elif flag == 2:
                        self.__players[i].setStack(self.__blind * (-2))
                        self.__players[i].setBet(self.__blind * 2)
                        self.__call = self.__blind * 2
                        self.setCurrentlyPos('next')
                        self.setCurrentlyPos('next')
                        self.setCurrentlyPos('next')
                        return


    def move(self, tgID, action):
        el = self.__currentlyPos
        print(f'{self.__currentlyPos.getFname()} is currently pos')
        if tgID == el.getID():
            if action == 'call':
                print(el.getID(), 'call')
                el.setStack(el.getBet() - self.__call)
                el.setBet(self.__call - el.getBet())
            elif action == 'fold':
                print(el.getID(), 'fold')
                el.setFold(False)
            elif action == 'bet':
                print(el.getID(), 'bet')
                el.setStack((-2) * self.__call)
                el.setBet(2*self.__call)
                self.__call *= 2
            elif action == 'check':
                print(el.getID(), 'check')
                if self.__call == 0:
                    pass
                else:
                    print("*check* error!!!")
            elif action == 'all-in':
                print(el.getID(), 'all-in')
                el.setBet(el.getStack())
                self.__call = el.getStack()
                el.setStack((-1) * el.getStack())
            elif action == 'raise':
                print(el.getID(), 'raise')
                print("*raise* error!!!")
            else:
                print('good')
            print("zapuskaiu setCurrentlyPos")
            self.setCurrentlyPos('next')
            return True
        else:
            return False


    def endStep(self, posPl):
        res = 0
        flag = 0
        for el in self.__players:
            if isinstance(el, Player):
                if el.getFold():
                    if flag == 0:
                        res = el.getBet()
                        flag += 1
                    else:
                        if res == el.getBet():
                            continue
                        else:
                            return False
        for el in self.__players:
            if isinstance(el, Player):
                if el.getPos():
                    if el.getID() == posPl:
                        return True
                    else:
                        return False



def f():
    a = Table()
    a.addPl('123', 'a', 1000, False, False, 0)
    a.addPl('234', 'w', 2000, False, False, 0)
    a.addPl('345', 'd', 3000, False, False, 0)
    a.addPl('456', 's', 4000, False, False, 0)


#f()

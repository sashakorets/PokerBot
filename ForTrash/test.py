from treys import Evaluator, Deck, Card
import pandas
import numpy as np

class PokerTable:
    def __init__(self, database, blind, ID, bank):
        self.deck = Deck()
        self.board = []
        self.database = database
        self.smallblind = blind
        self.bigblind = blind * 2
        self.call = blind * 2
        self.lasthand = ID
        self.bank = bank

    def play(self):
        self.setBoard(2)
        self.setCart(2)
        self.printInfo(3)
        self.rozdacha()
        self.printInfo(4)
        self.rozdacha()
        self.printInfo(5)
        self.rozdacha()

        self.winner()

        # refresh fold, all fold = 1
        self.setFold()
        # set lasthand / position
        self.setLastHand()

        self.setCart(1)
        self.setBoard(1)


    def rozdacha(self):
        keys = self.database.keys()
        i = self.lasthand
        while True:
            if self.allFold() == 2: #2 not fold
                if i in range(0, len(self.database)):
                    if self.database[list(keys)[i]][2] == 1:

                        self.workWithActions(input(f'{list(keys)[i]} !it is key! move:'), list(keys)[i])
                        if self.endCircle(list(keys)[i]):
                            # after end
                            # clean call, or other word call = 0
                            self.call = 0
                            # refresh bet, all bet = 0
                            self.setBet()
                            # add / del Player
                                # pass
                            return
                        i += 1
                    else:
                        i += 1
                        continue
                else:
                    i = 0
            elif self.allFold() == 1: #1 not fold
                # player win
                return
            else: #all fold
                return


    def workWithActions(self, action, key):
        if action == 'bet':
            if abs(self.database[key][1] - self.database[key][4]) < self.call*2:
                self.workWithActions('allin', key)
            else:
                self.database[key][1] -= self.call * 2
                self.database[key][4] += self.call * 2
                self.bank += self.call * 2
                self.call *= 2
        elif action == 'call':
            if abs(self.database[key][1] - self.database[key][4]) < self.call:
                self.workWithActions('allin', key)
            else:
                self.database[key][1] -= abs(self.call - self.database[key][4])
                self.bank += abs(self.call - self.database[key][4])
                self.database[key][4] = self.call
        elif not (action in ['allin', 'call', 'bet', 'check']): #fold
            self.database[key][2] = 0
        elif action == 'check':
            pass
        elif action == 'allin':
            self.bank += self.database[key][1]
            self.database[key][4] += self.database[key][1]
            self.call = self.database[key][4]
            self.database[key][1] = 0
        # elif action == 'raise':
        #     self.database[key][4] += 123
        #     self.pot += 123
        #     self.database[key][1] -= 123

    def allFold(self):
        flag = 0
        for i in self.database.keys():
            if self.database[i][2] == 1:
                flag += 1
        if flag >= 2:
            return 2
        elif flag == 1:
            return 1
        else:
            return 0

    def winner(self):
        evaluator = Evaluator()
        print(Card.print_pretty_cards(self.board))
        for i in self.database:
            print("!!!{} hand rank = {} {} {}".format(i, Card.print_pretty_cards(self.database[i][0]), evaluator.evaluate(self.board,self.database[i][0]),
                                                      evaluator.class_to_string(evaluator.get_rank_class(evaluator.evaluate(self.board, self.database[i][0])))))


    def sortKey(self):
        # counterclockwise
        res = []
        flag1 = 0
        for k in self.database.keys():
            if flag1 == 0:
                if self.database[k][3] == 1:
                    res.append(k)
                    flag1 = 1
                else:
                    continue
            else:
                res.append(k)
        for k in self.database.keys():
            if self.database[k][3] == 0:
                res.append(k)
            else:
                return res[::-1]


    def endCircle(self, keyPl):
        # and i == (self.lasthand - 1)
        temp = self.lasthand
        sortkeys = self.sortKey()
        while self.database[temp][2] == 0:
            temp = sortkeys.pop()

        res = 0
        flag = 0
        for key in self.database:
            if self.database[key][2] == 1:
                if flag == 0 :
                    res = self.database[key][4]
                    flag += 1
                else:
                    if res == self.database[key][4]:
                        continue
                    else:
                        return 0
        if temp == keyPl:
            return 1

    def addPlayer(self,key,info):
        if len(self.database) < 9:
            self.database[key] = info

    def delPlayer(self,key):
        if key in self.database.keys():
            self.database.pop(key)

    def setBoard(self, flag):
        # flag = 1 - clear
        # flag = 2 - new board
        if flag == 1:
            self.board = []
        elif flag == 2:
            self.board = self.deck.draw(5)
        else:
            return

    def setCart(self, flag):
        # flag = 1 - clear
        # flag = 2 - new hand
        if flag == 2:
            for i in self.database.keys():
                if self.database[i][2] == 0:
                    continue
                elif self.database[i][2] == 1:
                    self.database[i][0] = self.deck.draw(2)
        elif flag == 1:
            for i in self.database.keys():
                self.database[i][0] = 'hand'
        else:
            return

    def setLastHand(self):
        print('in this func set last hand or position')
        pass

    def setFold(self):
        for i in self.database.keys():
            self.database[i][2] = 1

    def setBet(self):
        for i in self.database.keys():
            self.database[i][4] = 0


    def printInfo(self, ftr:int):
        print("!--!"*15)
        with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
            print(pandas.DataFrame(self.database, index=['hand','stack','fold','button','bet']))
        print("board : ",Card.print_pretty_cards(self.board[:ftr]))
        print('call : ', self.call)
        print('bank : ', self.bank)
        print('last hand : ', self.lasthand)
        print("!--!" * 15)

# def main():
#     print('/*\\'*20, '1 circle')
#     a = PokerTable(database, 15, 'pl4', 0)
#     a.play()
#
#     print('/*\\'*20, '\n2 circle')
#     b = PokerTable(database, 30.123, 'pl5', 0)
#     b.play()

def main():
    evaluetor = Evaluator()
    deck = Deck()
    cards = deck.draw(2)
    board = deck.draw(5)
    print(cards)
    print(Card.print_pretty_cards(cards))
    print(evaluetor.evaluate(cards, board))
    print(evaluetor.get_rank_class(evaluetor.evaluate(cards,board)))
    cards = deck.draw(2)
    print(cards)
    print(Card.print_pretty_cards(cards))
    print(evaluetor.evaluate(cards, board))
    print(evaluetor.get_rank_class(evaluetor.evaluate(cards,board)))
    cards = deck.draw(2)
    print(cards)
    print(Card.print_pretty_cards(cards))
    print(evaluetor.evaluate(cards, board))

    print(board)
    print(Card.print_pretty_cards(board))


    print(evaluetor.get_rank_class(evaluetor.evaluate(cards,board)))



if __name__ == main():
    main()


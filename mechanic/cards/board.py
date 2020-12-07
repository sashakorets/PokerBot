from mechanic.cards.interfaceCard import interfaceCard

class Board(interfaceCard):
    def __init__(self):
        self.__board = '🃏🃏🃏🃏🃏'

    def setCard(self, deck, flag: bool):
        if flag:
            self.__board = deck.draw(5)
        else:
            self.__board = '🃏🃏🃏🃏🃏'
        return

    def getCard(self, flag: str):
        if flag == 'flop':
            return self.__board[0:3]
        elif flag == 'turn':
            return self.__board[0:4]
        elif flag == 'river':
            return self.__board[0:5]
        else:
            print("ERROR, no correct flag")

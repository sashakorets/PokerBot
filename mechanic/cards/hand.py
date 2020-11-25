class Hand:
    def __init__(self):
        self.__hand = '🃏🃏'

    def setHand(self, deck, flag: bool):
        if flag:
            self.__hand = deck.draw(2)
        else:
            self.__hand = '🃏🃏'
        return

    def getHand(self):
        return self.__hand

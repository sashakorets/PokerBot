from mechanic.cards.interfaceCard import interfaceCard

class Hand(interfaceCard):
    def __init__(self):
        self.__hand = '🃏🃏'

    def setCard(self, deck, flag: bool):
        if flag:
            self.__hand = deck.draw(2)
        else:
            self.__hand = '🃏🃏'
        return

    def getCard(self):
        return self.__hand

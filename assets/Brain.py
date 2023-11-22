import Card
import Deck
import Hand
import Board

class Brain:

    def __init__(self) -> None:
        self.deck = Deck()
        self.board = Board()
        self.hand = Hand()

    def how_many_cards(self, value=None, suit=None):    # returns the number of specific cards in the deck
        if not value:
            ...
        elif not suit:
            ...
        else:
            ...

    

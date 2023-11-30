from assets.Card import Card
from multipledispatch import dispatch

class Board:

    def __init__(self) -> None:
        self.cards = []
    
    def set_cards(self, cards):
        self.cards = cards

    def add_card(self, card:Card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards
    
    @dispatch()
    def return_suits(self):
        return [card.get_color() for card in self.cards]
    
    @dispatch(str)
    def return_suits(self, suit):
        return [card for card in self.cards if card.get_suit() == suit]


    @dispatch()
    def return_ranks(self):
        return [card.get_rank() for card in self.cards]
    
    @dispatch(int)
    def return_ranks(self, rank):
        return [card for card in self.cards if card.get_rank() == rank]
    
    def __str__(self):
        string = ""
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + "\t"
        if not string:
            string = "Board is empty"
        return string

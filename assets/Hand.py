from assets.Card import Card
from multipledispatch import dispatch

class Hand:

    def __init__(self) -> None:
        self.cards = []
    
    def get_cards(self):
        return self.cards
    
    def add_card(self, card: Card):
        if len(self.cards) < 2:
            self.cards.append(card)
        else:
            raise Exception("Hand is full")
        return card
    

    def remove_card(self, card: Card):
        if len(self.cards):
            self.cards.remove(card)
        else:
            raise Exception("Hand is empty")
        return card
    
    @dispatch()
    def return_suits(self):
        return [card.get_suit() for card in self.cards]
    
    @dispatch(str)
    def return_suits(self, suit):
        return [card for card in self.cards if card.get_suit() == suit]


    @dispatch()
    def return_ranks(self):
        return [card.get_rank() for card in self.cards]
    
    @dispatch(int)
    def return_ranks(self, rank):
        return [card for card in self.cards if card.get_rank() == rank]


    def __set_cards(self, card1: Card, card2: Card):
        return [card1, card2]

    
    def __str__(self):
        string = ""
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + "\t"
        if not string:
            string = "Hand is empty"
        return string
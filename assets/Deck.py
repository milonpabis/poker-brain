from assets.Card import Card
import random as rd
from multipledispatch import dispatch



class Deck:

    def __init__(self) -> None:
        self.suits = ["H", "D", "S", "C"]
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.complete = True

    def shuffle(self):          # not really useful
        rd.shuffle(self.cards)

    def reset(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.complete = True

    @dispatch(Card)
    def remove_card(self, card):
        self.cards.remove(card)
        self.complete = False
        return card

    @dispatch(str, int)
    def remove_card(self, suit, rank):
        card = [card for card in self.cards if card.get_suit() == suit and card.get_rank() == rank][0]
        self.cards.remove(card)
        self.complete = False
        return card
    
    @dispatch(str)
    def remove_card(self, suit):
        card = [card for card in self.cards if card.get_suit() == suit][0]
        self.cards.remove(card)

    @dispatch(Card)
    def add_card(self, card):
        self.cards.append(card)
        return card





    @dispatch(str, int)
    def __add_card(self, suit, rank):
        self.cards.append(Card(suit, rank))

    def return_suits(self, suit):
        return [card for card in self.cards if card.get_suit() == suit]
    
    def return_ranks(self, rank):  
        return [card for card in self.cards if card.get_rank() == rank]
    
    def get_cards(self):
        return self.cards

    def __str__(self):
        string = ""
        for i in range(len(self.cards)):
            if i % 13 == 0 and i != 0:
                string += "\n"
            string += str(self.cards[i]) + "\t"
        if not string:
            string = "Deck is empty"
        return string
 
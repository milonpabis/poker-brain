import Card
import random as rd

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Deck:

    def __init__(self) -> None:
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.complete = True

    def shuffle(self):          # not really useful
        rd.shuffle(self.cards)

    def remove_card(self, card):
        self.cards.remove(card)

    
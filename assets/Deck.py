import Card
import random as rd

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = [["Ace"], 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Deck:

    def __init__(self) -> None:
        self.cards = []
        self.complete = True
        self.create_deck()


    def create_deck(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):          # not really useful
        rd.shuffle(self.cards)

    def remove_card(self, card):
        self.cards.remove(card)

    
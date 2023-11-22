import Card
import Hand

class Board:

    def __init__(self) -> None:
        self.cards = []
    
    def set_cards(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

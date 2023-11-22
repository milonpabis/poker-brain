import Card

class Hand:

    def __init__(self) -> None:
        self.cards = self.set_cards()

    def set_cards(self, card1: Card, card2: Card):
        return [card1, card2]
    
    def get_cards(self):
        return self.cards
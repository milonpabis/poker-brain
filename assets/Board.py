from assets.Card import Card

class Board:

    def __init__(self) -> None:
        self.cards = []
    
    def set_cards(self, cards):
        self.cards = cards

    def add_card(self, card:Card):
        if len(self.cards) < 5:
            self.cards.append(card)
        else:
            raise Exception("Board is full")

    def get_cards(self):
        return self.cards
    
    def reset(self):
        self.cards = []
    
    def __str__(self):
        string = ""
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + "\t"
        if not string:
            string = "Board is empty"
        return string

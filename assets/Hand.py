from assets.Card import Card


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


    def __set_cards(self, card1: Card, card2: Card):
        return [card1, card2]

    
    def __str__(self):
        string = ""
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + "\t"
        if not string:
            string = "Hand is empty"
        return string
import Card
import Hand

class Board:

    def __init__(self) -> None:
        self.flop = self.set_flop()
        self.turn = self.set_turn()
        self.river = self.set_river()
    
    def set_flop(self, card1: Card, card2: Card, card3: Card):
        return [card1, card2, card3]
    
    def set_turn(self, card: Card):
        return card
    
    def set_river(self, card: Card):
        return card
    
    def get_flop(self):
        return self.flop
    
    def get_turn(self):
        return self.turn
    
    def get_river(self):
        return self.river

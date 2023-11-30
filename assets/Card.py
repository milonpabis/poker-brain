
class Card:
    
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def __str__(self):
        return str(self.rank) + str(self.suit)
        
    

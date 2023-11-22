CONVERTER = {"Ace": [1,14], "Jack": 11, "Queen": 12, "King": 13}

class Card:
    
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def convert_to_value(value):
        if value in CONVERTER:
            return CONVERTER[value]
        else:
            return value
        
    

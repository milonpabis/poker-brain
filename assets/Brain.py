from assets.Card import Card
from assets.Deck import Deck
from assets.Hand import Hand
from assets.Board import Board
from multipledispatch import dispatch

class Brain:

    def __init__(self) -> None:
        self.deck = Deck()
        self.board = Board()
        self.hand = Hand()


    @dispatch(Card)
    def add_hand_card(self, card):  # adds a card to the hand
        if len(self.hand.get_cards()) < 2:
            self.hand.add_card(self.deck.remove_card(card))
        return card
    

    @dispatch(str, int)
    def add_hand_card(self, suit, value):
        if len(self.hand.get_cards()) < 2:
            self.hand.add_card(self.deck.remove_card(suit, value))


    @dispatch(Card)
    def remove_hand_card(self, card):   # removes a card from the hand
        if len(self.hand.get_cards()):
            self.hand.remove_card(card)
            self.deck.add_card(card)
        return card


    @dispatch(str, int)
    def remove_hand_card(self, suit, value):
        if len(self.hand.get_cards()):
            self.hand.remove_card(suit, value)
            self.deck.add_card(suit, value)


    @dispatch(Card)
    def add_board_card(self, card): # adds a card to the board
        if len(self.board.get_cards()) < 5:
            self.board.add_card(self.deck.remove_card(card))
        return card


    @dispatch(str, int)
    def add_board_card(self, suit, value):
        if len(self.board.get_cards()) < 5:
            self.board.add_card(self.deck.remove_card(suit, value))










    def how_many_cards(self, value=None, suit=None):    # returns the number of specific cards in the deck
        if not value:
                 # returns the number of cards with the specific suit  // int
            return len(self.deck.return_suit(suit))
        elif not suit:
                 # returns the number of cards with the specific value  // int
            return len(self.deck.return_ranks(value))
        else:
                 # returns if card with the specific value and suit is in the deck    // bool 0 1
            return len(self.deck.return_ranks(value)) and len(self.deck.return_suit(suit))


    def calc_odds(self, value=None, suit=None):     # returns the odds of drawing a specific card
        if not value:
            return self.how_many_cards(suit=suit) / len(self.deck.get_cards())
        elif not suit:
            return self.how_many_cards(value=value) / len(self.deck.get_cards())
        else:
            return self.how_many_cards(value=value, suit=suit) / len(self.deck.get_cards())
        
        
    def color_chance(self):     # USING 2 ABOVE FUNCTIONS AND INFO ABOUT CARDS IN HAND AND BOARD
        ...

    def pair_chance(self):
        ...

    def two_pair_chance(self):
        ...

    def three_of_a_kind_chance(self):
        ...

    def straight_chance(self):
        ...

    def flush_chance(self):
        ...

    def full_house_chance(self):
        ...

    def four_of_a_kind_chance(self):
        ...

    def straight_flush_chance(self):
        ...

    def royal_flush_chance(self):
        ...

    

    

    

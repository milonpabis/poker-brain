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










    def how_many_cards_deck(self, rank=None, suit=None):    # returns the number of specific cards in the deck
        if not rank:
                 # returns the number of cards with the specific suit  // int
            return len(self.deck.return_suits(suit))
        elif not suit:
                 # returns the number of cards with the specific rank  // int
            return len(self.deck.return_ranks(rank))
        else:
                 # returns if card with the specific rank and suit is in the deck    // bool 0 1
            return len(self.deck.return_ranks(rank)) and len(self.deck.return_suits(suit))
        
    def how_many_cards_hand(self, value=None, suit=None):    # returns the number of specific cards in the hand
        if not value:
            return 


    def calc_odds(self, rank=None, suit=None):     # returns the odds of drawing a specific card
        if not rank:
            return self.how_many_cards_deck(suit=suit) / len(self.deck.get_cards())
        elif not suit:
            return self.how_many_cards_deck(value=rank) / len(self.deck.get_cards())
        else:
            return self.how_many_cards_deck(value=rank, suit=suit) / len(self.deck.get_cards())
        
        
    def flush_chance(self):     # USING 2 ABOVE FUNCTIONS AND INFO ABOUT CARDS IN HAND AND BOARD
        """
        returns the chance of getting color for given hand and board
        1. how many cards of the suit are in the hand and on board
        2. how many cards are to be drawn
        3. calculate the odds of drawing the color
        """
        result = 0
        hand_suits = set(self.hand.return_suits())
        for s in hand_suits:
            temp = 1
            amount = 5 - len(self.hand.return_suits(s)) - len(self.board.return_suits(s))
            for _ in range(amount):
                temp *= self.calc_odds(suit=s) # when calc_odds remove card from deck to simulate next drawing then add it back
            result += temp
        if result == 1:
            result = 0

        print(result) # return
                
        # ERRORS:
        # 1. does not take into account left cards to be drawn
        # 2. does not take into account simulation of removing the card from the deck

        # TODO: 
        # COPY DECK AND OPERATE ON IT!
        # SOMEHOW FIX ERROR NO. 1



    def pair_chance(self):
        ...

    def two_pair_chance(self):
        ...

    def three_of_a_kind_chance(self):
        ...

    def straight_chance(self):
        ...

    def full_house_chance(self):
        ...

    def four_of_a_kind_chance(self):
        ...

    def straight_flush_chance(self):
        ...

    def royal_flush_chance(self):
        ...

    

    

    

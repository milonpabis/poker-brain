from assets.Card import Card
from assets.Deck import Deck
from assets.Hand import Hand
from assets.Board import Board
from multipledispatch import dispatch
from copy import deepcopy

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










    def how_many_cards_deck(self, deck: Deck, rank=None, suit=None):    # returns the number of specific cards in the deck
        if not rank:
                 # returns the number of cards with the specific suit  // int
            return len(deck.return_suits(suit))
        elif not suit:
                 # returns the number of cards with the specific rank  // int
            return len(deck.return_ranks(rank))
        else:
                 # returns if card with the specific rank and suit is in the deck    // bool 0 1
            return len(deck.return_ranks(rank)) and len(deck.return_suits(suit))
        
    def how_many_cards_hand(self, value=None, suit=None):    # returns the number of specific cards in the hand
        if not value:
            return 


    def calc_odds(self, deck: Deck, rank=None, suit=None):     # returns the odds of drawing a specific card
        if not rank:
            return self.how_many_cards_deck(deck, suit=suit) / len(deck.get_cards())
        elif not suit:
            return self.how_many_cards_deck(deck, value=rank) / len(deck.get_cards())
        else:
            return self.how_many_cards_deck(deck, value=rank, suit=suit) / len(deck.get_cards())
        
        
    def flush_chance(self):     # USING 2 ABOVE FUNCTIONS AND INFO ABOUT CARDS IN HAND AND BOARD
        """
        returns the chance of getting flush for given hand and board
        1. how many cards of the suit are in the hand and on board
        2. how many cards are to be drawn
        3. calculate the odds of drawing the flush
        """

        result = 0
        hand_suits = set(self.hand.return_suits())      # unique suits in hand
        draws_left = 5 - len(self.board.get_cards())    # how many cards are to be drawn

        for s in hand_suits:                            # calculating the odds for each suit
            copied_deck = deepcopy(self.deck)               # copying the current deck status
            temp = 1
            amount = 5 - len(self.hand.return_suits(s)) - len(self.board.return_suits(s))   # how many do we need to get flush
            if amount < 1:                              # if we already have flush it will skip
                return 1
            if amount <= draws_left:                    # if we need to many it will skip
                for _ in range(amount):                  
                    temp *= self.calc_odds(copied_deck, suit=s)
                    copied_deck.remove_card(s)                     # simulating removal of the card from the deck
                result += temp

        return result



    def pair_chance(self):
        """
        returns the chance of getting pair for given hand and board
        1. check if there is a pair in hand
        2. check if there is a pair on board
        3. check if there is a pair in hand and on board
        4. if 3 above are false, calculate the odds of getting pair for every card in hand and board
        """
        ...

    def two_pair_chance(self):
        """
        returns the chance of getting two pair for given hand and board
        1. check if there is any pair already, if so calculate getting pair for all others
        2. if not, calculate the odds of getting two pair for every combination
        """
        ...

    def three_of_a_kind_chance(self):
        """
        returns the chance of getting three of a kind for given hand and board
        1. segregate all already drawn cards as values
        2. for every single value calculate odds of getting another two
        """
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

    

    

    

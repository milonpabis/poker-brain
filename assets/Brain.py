from assets.Card import Card
from assets.Deck import Deck
from assets.Hand import Hand
from assets.Board import Board
from multipledispatch import dispatch
from copy import deepcopy
from typing import List
from math import factorial

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





    @dispatch(list)
    def return_suits(self, list_of_cards: List[Card]):
        return [card.get_suit() for card in list_of_cards]
    
    @dispatch(list, str)
    def return_suits(self, list_of_cards: List[Card], suit):
        return [card for card in list_of_cards if card.get_suit() == suit]


    @dispatch(list)
    def return_ranks(self, list_of_cards: List[Card]):
        return [card.get_rank() for card in list_of_cards]
    
    @dispatch(list, int)
    def return_ranks(self, list_of_cards: List[Card], rank):
        return [card for card in list_of_cards if card.get_rank() == rank]










    def how_many_cards(self, list_of_cards: List[Card], rank=None, suit=None):    # returns the number of specific cards in the list
        if not rank:
                 # returns the number of cards with the specific suit  // int
            return len(self.return_suits(list_of_cards, suit))
        elif not suit:
                 # returns the number of cards with the specific rank  // int
            return len(self.return_ranks(list_of_cards, rank))
        else:
                 # returns if card with the specific rank and suit is in the deck    // bool 0 1
            return len(self.return_ranks(list_of_cards, rank)) and len(self.return_suits(list_of_cards, suit))


    def calc_odds(self, list_of_cards: List[Card], rank=None, suit=None):     # returns the odds of drawing a specific card for given list
        if not rank:
            return self.how_many_cards(list_of_cards, suit=suit) / len(list_of_cards)
        elif not suit:
            return self.how_many_cards(list_of_cards, value=rank) / len(list_of_cards)
        else:
            return self.how_many_cards(list_of_cards, value=rank, suit=suit) / len(list_of_cards)
        
        
    def flush_chance(self):     # USING 2 ABOVE FUNCTIONS AND INFO ABOUT CARDS IN HAND AND BOARD
        """
        returns the chance of getting flush for given hand and board
        1. check if there is a flush in hand||board -> return 1
        2. if not, calculate the odds of drawing the flush
        """

        # TODO:
        # - combine hand and board DONE
        # - calculate for the whole hand||board not only for hand combinations DONE
        # - newton equation

        cards = self.hand.get_cards() + self.board.get_cards()    # combining hand and board

        result = 0
        unique_suits = set(self.return_suits(cards))      # unique suits
        draws_left = 5 - len(self.board.get_cards())    # how many cards are to be drawn

        for s in unique_suits:                            # calculating the odds for each suit
            temp = 1
            amount = 5 - len(self.return_suits(cards, s))   # how many do we need to get flush
            if amount < 1:                              # if we already have flush it will skip
                return 1
            if amount > draws_left:
                continue
            temp = self.newton(13 - (5 - amount), amount) * self.newton(52 - amount - len(cards), draws_left - amount) / self.newton(52 - len(cards), draws_left)
            result += temp

        return result



    def pair_chance(self):
        """
        returns the chance of getting pair for given hand and board
        1. check if there is a pair in hand||board -> return 1
        2. if not, calculate the odds of getting pair for every card in hand||board
        """
        cards = self.hand.get_cards() + self.board.get_cards()

        ...

    def two_pair_chance(self):
        """
        returns the chance of getting two pair for given hand and board
        1. check if there are two pair already -> return 1
        2. check if there is any pair already -> calculate getting pair for all others
        3. if not, calculate the odds of getting two pair for every combination
        """
        ...

    def three_of_a_kind_chance(self):
        """
        returns the chance of getting three of a kind for given hand and board
        1. check if there is three of a kind already -> return 1
        2. check if there is a pair for given hand||board -> calculate odds to get another one
        3. for every single value calculate odds of getting another two
        """
        ...

    def straight_chance(self):
        """
        returns the chance of getting straight for given hand and board
        1. ...
        2. ...
        """
        ...

    def full_house_chance(self):
        """
        returns the chance of getting full house for given hand and board
        1. check if there is a full house already -> return 1
        2. check if there is a pair in hand||board -> calculate odds of getting three of a kind
        3. check if there is a three of a kind in hand||board -> calculate odds of getting pair
        4. if not, calculate the odds of getting full house for every combination
        """
        ...

    def four_of_a_kind_chance(self):
        """
        returns the chance of getting four of a kind for given hand and board
        1. check if there is a four of a kind already -> return 1
        2. for every existing card/cards calculate odds of getting another three/two/one
        """
        ...

    def straight_flush_chance(self):
        """
        returns the chance of getting straight flush for given hand and board
        1. ...
        2. ...
        """
        ...

    def royal_flush_chance(self):
        """
        returns the chance of getting royal flush for given hand and board
        1. ...
        2. ...
        """
        ...

    

    def newton(self, n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    

    

    

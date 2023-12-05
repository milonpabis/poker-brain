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
            return self.how_many_cards(list_of_cards, rank=rank) / len(list_of_cards)
        else:
            return self.how_many_cards(list_of_cards, rank=rank, suit=suit) / len(list_of_cards)
        



        # TODO:
        # 1. flush -> work on every suit not only unique in hand||board
        # 2. straight -> dont count overlapping straights / add ace conversion to 1
        # 3. straight flush -> do
        # 4. royal flush -> do
        # 5. full house -> find bug and fix it ( sometimes is 2x higher than three of a kind ) **DONE** ( PROBABLY :) )
        # 6. two pair -> find bug and fix it ( shows 1 even if there is only 1 pair)   **DONE**
        
        
    def flush_chance(self):     # USING 2 ABOVE FUNCTIONS AND INFO ABOUT CARDS IN HAND AND BOARD
        """
        returns the chance of getting flush for given hand and board
        1. check if there is a flush in hand||board -> return 1
        2. if not, calculate the odds of drawing the flush
        """

        cards = self.hand.get_cards() + self.board.get_cards()    # combining hand and board

        result = 0
        unique_suits = set(self.return_suits(cards))      # unique suits
        draws_left = 5 - len(self.board.get_cards())    # how many cards are to be drawn

        for s in unique_suits:                            # calculating the odds for each suit
            s_drawn = len(self.return_suits(cards, s))      # how many cards of this suit are already drawn
            temp = 1
            amount = 5 - s_drawn   # how many do we need to get flush
            if amount < 1:                              # if we already have flush it will skip
                return 1
            if amount > draws_left:
                continue
            temp = self.newton(13 - s_drawn, amount) * self.newton(52 - amount - len(cards), draws_left - amount) / self.newton(52 - len(cards), draws_left)
            result += temp

        return result

    # TO UNDERSTAND LOGIC UNDERNEATH, CHECK THE FLUSH CHANCE FUNCTION !!!

    def pair_chance(self):
        """
        returns the chance of getting pair for given hand and board
        1. check if there is a pair in hand||board -> return 1
        2. if not, calculate the odds of getting pair for every card in hand||board
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())

        for r in self.deck.ranks:                               # simple combinatorics equation
            r_drawn = len(self.return_ranks(cards, r))
            amount = 2 - r_drawn
            if amount < 1:
                return 1
            if amount > draws_left:
                continue
            temp = self.newton(4 - r_drawn, amount) * self.newton(52 - amount - len(cards), draws_left - amount) / self.newton(52 - len(cards), draws_left)
            result += temp
        return result
    

    def two_pair_chance(self):
        """
        returns the chance of getting two pair for given hand and board
        1. check if there are two pair already -> return 1
        2. check if there is any pair already -> calculate getting pair for all others
        3. if not, calculate the odds of getting two pair for every combination
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())

        t = []
        for r1 in self.deck.ranks:                        
            t.append(r1)                                        # don't want to calculate the same pair twice
            temp_list = set(self.deck.ranks) - set(t)           # temp list of ranks without the ones already calculated
            for r2 in temp_list:
                r1_drawn = len(self.return_ranks(cards, r1))
                r2_drawn = len(self.return_ranks(cards, r2))
                amount_r1 = 2 - r1_drawn
                amount_r2 = 2 - r2_drawn
                if amount_r1 < 1 and amount_r2 < 1:
                    return 1
                if amount_r1 < 1:
                    amount_r1 = 0
                if amount_r2 < 1:
                    amount_r2 = 0
                if amount_r1 + amount_r2 > draws_left:
                    continue
                temp = self.newton(4 - r1_drawn, amount_r1) * self.newton(4 - r2_drawn, amount_r2) * self.newton(52 - amount_r1 - amount_r2 - len(cards), draws_left - amount_r1 - amount_r2) / self.newton(52 - len(cards), draws_left)
                result += temp
        return result


    def three_of_a_kind_chance(self):
        """
        returns the chance of getting three of a kind for given hand and board
        1. check if there is three of a kind already -> return 1
        2. check if there is a pair for given hand||board -> calculate odds to get another one
        3. for every single value calculate odds of getting another two
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())

        for r in self.deck.ranks:
            r_drawn = len(self.return_ranks(cards, r))
            amount = 3 - r_drawn
            if amount < 1:
                return 1
            if amount > draws_left:
                continue
            temp = self.newton(4 - r_drawn, amount) * self.newton(52 - amount - len(cards), draws_left - amount) / self.newton(52 - len(cards), draws_left)
            result += temp
        return result

    def straight_chance(self):
        """
        returns the chance of getting straight for given hand and board
        1. check if there is straight already -> return 1
        2. check if possible to get a straight with given hand||board
        3. find all rank combinations that can make a straight
        4. calculate odds of getting a straight for every combination
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())
        
        for r1 in self.deck.ranks: # check if straight on board
             if all(r1 + i in self.return_ranks(cards) for i in range(5)):
                return 1

        for r1 in self.deck.ranks[:-4]: # can't make a straight with last 4 ranks
            ranks_needed = [r for r in range(r1, r1 + 5) if r not in self.return_ranks(cards)]

            if len(ranks_needed) > draws_left:
                continue

            temp_odds = 1
            for r2 in ranks_needed:
                r2_drawn = len(self.return_ranks(cards, r2))
                temp_odds *= self.newton(4 - r2_drawn, 1)

            result += temp_odds / self.newton(52 - len(cards), len(ranks_needed))

        return result

    def full_house_chance(self):
        """
        returns the chance of getting full house for given hand and board
        1. check if there is a full house already -> return 1
        2. check if there is a pair in hand||board -> calculate odds of getting three of a kind
        3. check if there is a three of a kind in hand||board -> calculate odds of getting pair
        4. if not, calculate the odds of getting full house for every combination
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())

        r1_alones_done = []
        r2_alones_done = []

        for r1 in self.deck.ranks:
            temp_list = set(self.deck.ranks) - set([r1])                 # same as in two pair, however we must calculate every pair ( pair&three != three&pair )
            for r2 in temp_list:
                r1_drawn = len(self.return_ranks(cards, r1))
                r2_drawn = len(self.return_ranks(cards, r2))
                amount_r1 = 3 - r1_drawn
                amount_r2 = 2 - r2_drawn
                if amount_r1 < 1 and amount_r2 < 1:
                    return 1
                if amount_r1 < 1:
                    amount_r1 = 0
                    if r2 in r2_alones_done:        # there was a fucking bug! 
                        continue                    # simply:
                    else:                           # for different pairs (r1, r2), when for ex. amount_r2 was 0 ( already fulfilled )
                        r2_alones_done.append(r2)   # r1 was calculated alone, and if a similiar situation happened for the same r1
                if amount_r2 < 1:                   # it calculated odds for r1 alone again
                    amount_r2 = 0                   # so there are two lists, that store information about whether it was already 
                    if r1 in r1_alones_done:        # calculated, if so -> skip, if not -> store
                        continue                    
                    else:                           
                        r1_alones_done.append(r1)  
                if amount_r1 + amount_r2 > draws_left:
                    continue 
                #print("FULL", "r1:", r1, "r2:", r2, "amount_r1:", amount_r1, "amount_r2:", amount_r2)
                temp = self.newton(4 - r1_drawn, amount_r1) * self.newton(4 - r2_drawn, amount_r2) * self.newton(52 - amount_r1 - amount_r2 - len(cards), draws_left - amount_r1 - amount_r2) / self.newton(52 - len(cards), draws_left)
                result += temp
        return result

    def four_of_a_kind_chance(self):
        """
        returns the chance of getting four of a kind for given hand and board
        1. check if there is a four of a kind already -> return 1
        2. for every existing card/cards calculate odds of getting another three/two/one
        """
        cards = self.hand.get_cards() + self.board.get_cards()
        result = 0
        draws_left = 5 - len(self.board.get_cards())
        
        for r in self.deck.ranks:
            r_drawn = len(self.return_ranks(cards, r))
            amount = 4 - r_drawn
            if amount < 1:
                return 1
            if amount > draws_left:
                continue
            temp = self.newton(4 - r_drawn, amount) * self.newton(52 - amount - len(cards), draws_left - amount) / self.newton(52 - len(cards), draws_left)
            result += temp
        
        return result

    def straight_flush_chance(self):
        """
        returns the chance of getting straight flush for given hand and board
        1. ...
        2. ...
        """
        

        return "NOT IMPLEMENTED"

    def royal_flush_chance(self):
        """
        returns the chance of getting royal flush for given hand and board
        1. ...
        2. ...
        """
        

        return "NOT IMPLEMENTED"

    

    def newton(self, n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))
    
    def calculate(self):
        """
        returns a list of all odds for given hand and board
        """
        result = []
        result.append(self.pair_chance())
        result.append(self.two_pair_chance())
        result.append(self.three_of_a_kind_chance())
        result.append(self.straight_chance())
        result.append(self.flush_chance())
        result.append(self.full_house_chance())
        result.append(self.four_of_a_kind_chance())
        result.append(self.straight_flush_chance())
        result.append(self.royal_flush_chance())
        return result

    def reset(self):
        self.deck.reset()
        self.hand.reset()
        self.board.reset()

    

    

    

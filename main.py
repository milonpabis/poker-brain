from assets.Brain import Brain

if __name__ == "__main__":
    
    game = Brain()
    #print(game.deck)
    #print(game.hand)
    #print(game.board)

    game.add_hand_card("H", 2)
    game.add_hand_card("H", 3)

    #print(game.deck)
    #print(game.hand)

    game.add_board_card("C", 4)
    game.add_board_card("C", 14)
    game.add_board_card("C", 12)
    game.add_board_card("H", 11)

    game.flush_chance()

    print(game.deck)
    print(game.board)
    print(game.hand)


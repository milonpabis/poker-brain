from assets.Brain import Brain
from gui import MainWindow, QApplication

if __name__ == "__main__":
    
    game = Brain()
    #print(game.deck)
    #print(game.hand)
    #print(game.board)

    game.add_hand_card("H", 10)
    game.add_hand_card("S", 12)

    #print(game.deck)
    #print(game.hand)

    game.add_board_card("S", 13)
    game.add_board_card("S", 2)
    game.add_board_card("S", 14)
    
    
    
    #game.add_board_card("H", 11)
    #game.add_board_card("C", 10)

    pair_chance = game.pair_chance()
    print("PAIR CHANCE: ", pair_chance)
    two_pair_chance = game.two_pair_chance()
    print("TWO PAIR CHANCE: ", two_pair_chance)
    three_of_a_kind_chance = game.three_of_a_kind_chance()
    print("THREE OF A KIND CHANCE: ", three_of_a_kind_chance)
    straight_chance = game.straight_chance()
    print("STRAIGHT CHANCE: ", straight_chance)
    flush_chance = game.flush_chance()
    print("FLUSH CHANCE: ", flush_chance)
    full_house_chance = game.full_house_chance()
    print("FULL HOUSE CHANCE: ", full_house_chance)
    four_of_a_kind_chance = game.four_of_a_kind_chance()
    print("FOUR OF A KIND CHANCE: ", four_of_a_kind_chance)
    straight_flush_chance = game.straight_flush_chance()
    print("STRAIGHT FLUSH CHANCE: ", straight_flush_chance)
    royal_flush_chance = game.royal_flush_chance()
    print("ROYAL FLUSH CHANCE: ", royal_flush_chance)

    print(game.deck)
    print(game.board)
    print(game.hand)

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

    


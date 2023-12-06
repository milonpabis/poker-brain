from assets.UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from assets.UI.CardView import CardView, QListWidgetItem, QPoint, Qt, QListWidget, QPixmap
from assets.Brain import Brain


# TODO:
# - repair reset function! DONE

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowTitle("Poker Odds Calculator")


        self.current_values = [0, 0, 0, 0, 0, 0, 0]
        self.brain = Brain()    # logic instance
        self._setupView()       # setting up widgets
        

        




    def reset(self):
        self.brain.reset()
        self.initialize_board()
        print("debug: reset")

    def calculate(self):
        print(self.current_values)
        can_calculate = True
        
        hand1 = self.current_values[5]
        hand2 = self.current_values[6]
        board1 = self.current_values[0]
        board2 = self.current_values[1]
        board3 = self.current_values[2]
        board4 = self.current_values[3]
        board5 = self.current_values[4]

        if not hand1 or not hand2:
            can_calculate = False
        else:
            print(hand1, hand2)
            self.brain.add_hand_card(hand1[0], int(hand1[1:]))
            self.brain.add_hand_card(hand2[0], int(hand2[1:]))

        if board1:
            self.brain.add_board_card(board1[0], int(board1[1:]))
        if board2:
            self.brain.add_board_card(board2[0], int(board2[1:]))
        if board3:
            self.brain.add_board_card(board3[0], int(board3[1:]))
        if board4:
            self.brain.add_board_card(board4[0], int(board4[1:]))
        if board5:
            self.brain.add_board_card(board5[0], int(board5[1:]))

        if can_calculate:
            result = self.brain.calculate()
            print(result)
            result = list(map(lambda x: round(x*100, 2) if isinstance(x, float) or isinstance(x, int) else x, result))
            print(result)

            self.l_pairOdd.setText(str(result[0]) + "%")
            self.l_twoPairOdd.setText(str(result[1]) + "%")
            self.l_ThreeOdd.setText(str(result[2]) + "%")
            self.l_straightOdd.setText(str(result[3]) + "%")
            self.l_flushOdd.setText(str(result[4]) + "%")
            self.l_fullOdd.setText(str(result[5]) + "%")
            self.l_fourOdd.setText(str(result[6]) + "%")
            self.l_straightFlushOdd.setText(str(result[7]) + "%")
            self.l_royalFlushOdd.setText(str(result[8]) + "%")

        self.brain.reset()

        print("debug: calculate")

    def initialize_board(self):
        self.lbBoard1.setPixmap(QPixmap())
        self.lbBoard2.setPixmap(QPixmap())
        self.lbBoard3.setPixmap(QPixmap())
        self.lbBoard4.setPixmap(QPixmap())
        self.lbBoard5.setPixmap(QPixmap())
        self.lbHand1.setPixmap(QPixmap())
        self.lbHand2.setPixmap(QPixmap())

        self.l_highOdd.setText("---")
        self.l_pairOdd.setText("---")
        self.l_twoPairOdd.setText("---")
        self.l_ThreeOdd.setText("---")
        self.l_straightOdd.setText("---")
        self.l_flushOdd.setText("---")
        self.l_fullOdd.setText("---")
        self.l_fourOdd.setText("---")
        self.l_straightFlushOdd.setText("---")
        self.l_royalFlushOdd.setText("---")

        self.listHearts.clear()
        self.listClubs.clear()
        self.listDiamonds.clear()
        self.listSpades.clear()

        self.current_values = [0, 0, 0, 0, 0, 0, 0]

        cards = self.brain.deck.get_cards()
        for card in cards:
            suit = card.get_suit()
            rank = card.get_rank()
            card = CardView(f"{suit}{rank}")
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())
            if suit == "H":
                self.listHearts.addItem(item)
                self.listHearts.setItemWidget(item, card)
            elif suit == "D":
                self.listDiamonds.addItem(item)
                self.listDiamonds.setItemWidget(item, card)
            elif suit == "S":
                self.listSpades.addItem(item)
                self.listSpades.setItemWidget(item, card)
            elif suit == "C":
                self.listClubs.addItem(item)
                self.listClubs.setItemWidget(item, card)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        pos = event.pos()
        widget = event.source()
        lb1_cor = self.lbBoard1.mapFrom(self, pos)  # board 1
        lb2_cor = self.lbBoard2.mapFrom(self, pos)  # board 2
        lb3_cor = self.lbBoard3.mapFrom(self, pos)  # board 3
        lb4_cor = self.lbBoard4.mapFrom(self, pos)  # board 4
        lb5_cor = self.lbBoard5.mapFrom(self, pos)  # board 5
        lh1_cor = self.lbHand1.mapFrom(self, pos)   # hand 1
        lh2_cor = self.lbHand2.mapFrom(self, pos)   # hand 2


        if lb1_cor.x() > 0 and lb1_cor.y() > 0 and lb1_cor.x() < 100 and lb1_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[0] = widget.value
            self.lbBoard1.setPixmap(widget.pixmap())
            self._remove_card(widget)

        if lb2_cor.x() > 0 and lb2_cor.y() > 0 and lb2_cor.x() < 100 and lb2_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[1] = widget.value
            self.lbBoard2.setPixmap(widget.pixmap())
            self._remove_card(widget)

        if lb3_cor.x() > 0 and lb3_cor.y() > 0 and lb3_cor.x() < 100 and lb3_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[2] = widget.value
            self.lbBoard3.setPixmap(widget.pixmap())
            self._remove_card(widget)

        if lb4_cor.x() > 0 and lb4_cor.y() > 0 and lb4_cor.x() < 100 and lb4_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[3] = widget.value
            self.lbBoard4.setPixmap(widget.pixmap())
            self._remove_card(widget)

        if lb5_cor.x() > 0 and lb5_cor.y() > 0 and lb5_cor.x() < 100 and lb5_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[4] = widget.value
            self.lbBoard5.setPixmap(widget.pixmap())
            self._remove_card(widget)
        
        if lh1_cor.x() > 0 and lh1_cor.y() > 0 and lh1_cor.x() < 100 and lh1_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[5] = widget.value
            self.lbHand1.setPixmap(widget.pixmap())
            self._remove_card(widget)

        if lh2_cor.x() > 0 and lh2_cor.y() > 0 and lh2_cor.x() < 100 and lh2_cor.y() < 150:
            print("debug: dropEvent")
            self.current_values[6] = widget.value
            self.lbHand2.setPixmap(widget.pixmap())
            self._remove_card(widget)
        
        event.accept()


    def _remove_card(self, cardView):
        row = self._find_card_in_lists(cardView, self.listHearts)
        print("H", row)
        if row != -1:
            self.listHearts.takeItem(row)
            return
        row = self._find_card_in_lists(cardView, self.listDiamonds)
        print("D", row)
        if row != -1:
            self.listDiamonds.takeItem(row)
            return
        row = self._find_card_in_lists(cardView, self.listSpades)
        print("S", row)
        if row != -1:
            self.listSpades.takeItem(row)
            return
        row = self._find_card_in_lists(cardView, self.listClubs)
        print("C", row)
        if row != -1:
            self.listClubs.takeItem(row)
            return

    def _find_card_in_lists(self, cardView, list_widget):
        for row in range(list_widget.count()):
            item = list_widget.item(row)
            if list_widget.itemWidget(item) is cardView:
                return row
        return -1
    
    def _setupView(self):
        self.btCalculate.clicked.connect(self.calculate)
        self.btReset.clicked.connect(self.reset)

        self.listHearts.setFlow(QListWidget.LeftToRight)
        self.listHearts.setSpacing(10)

        self.listDiamonds.setFlow(QListWidget.LeftToRight)
        self.listDiamonds.setSpacing(10)

        self.listSpades.setFlow(QListWidget.LeftToRight)
        self.listSpades.setSpacing(10)

        self.listClubs.setFlow(QListWidget.LeftToRight)
        self.listClubs.setSpacing(10)

        self.lbBoard1.setScaledContents(True)
        self.lbBoard2.setScaledContents(True)
        self.lbBoard3.setScaledContents(True)
        self.lbBoard4.setScaledContents(True)
        self.lbBoard5.setScaledContents(True)
        self.lbHand1.setScaledContents(True)
        self.lbHand2.setScaledContents(True)
        self.initialize_board()





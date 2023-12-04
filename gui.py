from assets.UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from assets.UI.CardView import CardView, QListWidgetItem, QPoint, Qt, QListWidget
from assets.Brain import Brain


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowTitle("Poker Odds Calculator")
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

        self.brain = Brain()

        self.initialize_board()

    def reset(self):
        #self.brain.reset()
        self.initialize_board()
        print("debug: reset")

    def calculate(self):
        print("debug: calculate")

    def initialize_board(self):
        self.lbBoard1.setText("")
        self.lbBoard2.setText("")
        self.lbBoard3.setText("")
        self.lbBoard4.setText("")
        self.lbBoard5.setText("")
        self.lbHand1.setText("")
        self.lbHand2.setText("")

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
            self.lbBoard1.setText(widget.value)

        if lb2_cor.x() > 0 and lb2_cor.y() > 0 and lb2_cor.x() < 100 and lb2_cor.y() < 150:
            print("debug: dropEvent")
            self.lbBoard2.setText(widget.value)

        if lb3_cor.x() > 0 and lb3_cor.y() > 0 and lb3_cor.x() < 100 and lb3_cor.y() < 150:
            print("debug: dropEvent")
            self.lbBoard3.setText(widget.value)

        if lb4_cor.x() > 0 and lb4_cor.y() > 0 and lb4_cor.x() < 100 and lb4_cor.y() < 150:
            print("debug: dropEvent")
            self.lbBoard4.setText(widget.value)

        if lb5_cor.x() > 0 and lb5_cor.y() > 0 and lb5_cor.x() < 100 and lb5_cor.y() < 150:
            print("debug: dropEvent")
            self.lbBoard5.setText(widget.value)
        
        if lh1_cor.x() > 0 and lh1_cor.y() > 0 and lh1_cor.x() < 100 and lh1_cor.y() < 150:
            print("debug: dropEvent")
            self.lbHand1.setText(widget.value)

        if lh2_cor.x() > 0 and lh2_cor.y() > 0 and lh2_cor.x() < 100 and lh2_cor.y() < 150:
            print("debug: dropEvent")
            self.lbHand2.setText(widget.value)
        
        event.accept()


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 600)
        MainWindow.setMinimumSize(QSize(1300, 600))
        MainWindow.setMaximumSize(QSize(1300, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1300, 600))
        self.centralwidget.setMaximumSize(QSize(1300, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(300, 0))
        self.frame_13.setMaximumSize(QSize(300, 16777215))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_13)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Cooper Black"])
        font.setPointSize(10)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(0, 158, 253);\n"
"color: white;")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.l_highOdd = QLabel(self.groupBox)
        self.l_highOdd.setObjectName(u"l_highOdd")
        self.l_highOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.l_highOdd)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(0, 136, 214);\n"
"background-color: rgb(0, 146, 231);\n"
"color: white;")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.l_pairOdd = QLabel(self.groupBox_2)
        self.l_pairOdd.setObjectName(u"l_pairOdd")
        self.l_pairOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.l_pairOdd)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.frame_13)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"background-color: rgb(0, 143, 226);\n"
"background-color: rgb(0, 129, 203);\n"
"color: white;")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.l_twoPairOdd = QLabel(self.groupBox_7)
        self.l_twoPairOdd.setObjectName(u"l_twoPairOdd")
        self.l_twoPairOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.l_twoPairOdd)


        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(self.frame_13)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(0, 98, 154);\n"
"color: white;")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.l_ThreeOdd = QLabel(self.groupBox_3)
        self.l_ThreeOdd.setObjectName(u"l_ThreeOdd")
        self.l_ThreeOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.l_ThreeOdd)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_8 = QGroupBox(self.frame_13)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet(u"background-color: rgb(139, 0, 253);\n"
"color: white;")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.l_straightOdd = QLabel(self.groupBox_8)
        self.l_straightOdd.setObjectName(u"l_straightOdd")
        self.l_straightOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.l_straightOdd)


        self.verticalLayout_6.addWidget(self.groupBox_8)

        self.groupBox_4 = QGroupBox(self.frame_13)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"background-color: rgb(121, 0, 226);\n"
"color: white;")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.l_flushOdd = QLabel(self.groupBox_4)
        self.l_flushOdd.setObjectName(u"l_flushOdd")
        self.l_flushOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.l_flushOdd)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.groupBox_10 = QGroupBox(self.frame_13)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet(u"background-color: rgb(102, 0, 191);\n"
"color: white;")
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.l_fullOdd = QLabel(self.groupBox_10)
        self.l_fullOdd.setObjectName(u"l_fullOdd")
        self.l_fullOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.l_fullOdd)


        self.verticalLayout_6.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.frame_13)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet(u"background-color: rgb(84, 0, 157);\n"
"color: white;")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.l_fourOdd = QLabel(self.groupBox_9)
        self.l_fourOdd.setObjectName(u"l_fourOdd")
        self.l_fourOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.l_fourOdd)


        self.verticalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_5 = QGroupBox(self.frame_13)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"background-color: rgb(158, 0, 68);\n"
"color: white;")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.l_straightFlushOdd = QLabel(self.groupBox_5)
        self.l_straightFlushOdd.setObjectName(u"l_straightFlushOdd")
        self.l_straightFlushOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.l_straightFlushOdd)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_13)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(127, 0, 54);\n"
"color: white;")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.l_royalFlushOdd = QLabel(self.groupBox_6)
        self.l_royalFlushOdd.setObjectName(u"l_royalFlushOdd")
        self.l_royalFlushOdd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.l_royalFlushOdd)


        self.verticalLayout_6.addWidget(self.groupBox_6)


        self.horizontalLayout.addWidget(self.frame_13)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 0))
        self.frame.setMaximumSize(QSize(700, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 350))
        self.frame_3.setMaximumSize(QSize(16777215, 350))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(66, 175, 27);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:1, y2:0.483, stop:0 rgba(2, 136, 24, 255), stop:1 rgba(37, 189, 35, 255));")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(100, 150))
        self.frame_7.setMaximumSize(QSize(100, 150))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbBoard1 = QLabel(self.frame_7)
        self.lbBoard1.setObjectName(u"lbBoard1")
        self.lbBoard1.setMinimumSize(QSize(0, 150))
        self.lbBoard1.setMaximumSize(QSize(16777215, 150))
        self.lbBoard1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 3px solid black\n"
"")

        self.verticalLayout_2.addWidget(self.lbBoard1)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(100, 150))
        self.frame_8.setMaximumSize(QSize(100, 150))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbBoard2 = QLabel(self.frame_8)
        self.lbBoard2.setObjectName(u"lbBoard2")
        self.lbBoard2.setStyleSheet(u"border: 3px solid black;")

        self.verticalLayout_4.addWidget(self.lbBoard2)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(100, 150))
        self.frame_10.setMaximumSize(QSize(100, 150))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbBoard3 = QLabel(self.frame_10)
        self.lbBoard3.setObjectName(u"lbBoard3")
        self.lbBoard3.setStyleSheet(u"border: 3px solid black;")

        self.horizontalLayout_6.addWidget(self.lbBoard3)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 0))
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(20, 223, 44);\n"
"background-color: rgb(66, 175, 27);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:1, y2:0.483, stop:0 rgba(37, 189, 35, 255), stop:1 rgba(2, 136, 24, 255));")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(70)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 0, 30, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(100, 150))
        self.frame_11.setMaximumSize(QSize(100, 150))
        self.frame_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbBoard4 = QLabel(self.frame_11)
        self.lbBoard4.setObjectName(u"lbBoard4")
        self.lbBoard4.setStyleSheet(u"border: 3px solid black;")

        self.horizontalLayout_8.addWidget(self.lbBoard4)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 150))
        self.frame_12.setMaximumSize(QSize(100, 150))
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbBoard5 = QLabel(self.frame_12)
        self.lbBoard5.setObjectName(u"lbBoard5")
        self.lbBoard5.setStyleSheet(u"border: 3px solid black;")

        self.horizontalLayout_7.addWidget(self.lbBoard5)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(66, 175, 27);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:1, y2:0.483, stop:0 rgba(2, 136, 24, 255), stop:0.65 rgba(37, 189, 35, 255), stop:1 rgba(2, 136, 24, 255));")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(200, 0, 200, 0)
        self.lbHand1 = QLabel(self.frame_4)
        self.lbHand1.setObjectName(u"lbHand1")
        self.lbHand1.setMinimumSize(QSize(100, 150))
        self.lbHand1.setMaximumSize(QSize(100, 150))
        self.lbHand1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 3px solid black;")

        self.horizontalLayout_5.addWidget(self.lbHand1)

        self.lbHand2 = QLabel(self.frame_4)
        self.lbHand2.setObjectName(u"lbHand2")
        self.lbHand2.setMinimumSize(QSize(100, 150))
        self.lbHand2.setMaximumSize(QSize(100, 150))
        self.lbHand2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 3px solid black;")

        self.horizontalLayout_5.addWidget(self.lbHand2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"background-color: rgb(66, 175, 27);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:1, y2:0.483, stop:0 rgba(2, 136, 24, 255), stop:0.65 rgba(37, 189, 35, 255), stop:1 rgba(2, 136, 24, 255));")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(200, 0, 250, 0)
        self.btReset = QPushButton(self.frame_5)
        self.btReset.setObjectName(u"btReset")
        self.btReset.setMinimumSize(QSize(50, 0))
        self.btReset.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Cooper Black"])
        font1.setPointSize(10)
        self.btReset.setFont(font1)
        self.btReset.setStyleSheet(u"QPushButton {\n"
"border: 3px solid black;\n"
"background-color: rgb(89, 255, 28);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 2px solid black;\n"
"background-color: rgb(89, 255, 28);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"border: 2px solid black;\n"
"background-color: rgb(13, 173, 26);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.btReset)

        self.btCalculate = QPushButton(self.frame_5)
        self.btCalculate.setObjectName(u"btCalculate")
        self.btCalculate.setMinimumSize(QSize(200, 30))
        self.btCalculate.setMaximumSize(QSize(200, 30))
        font2 = QFont()
        font2.setFamilies([u"Cooper Black"])
        font2.setPointSize(16)
        self.btCalculate.setFont(font2)
        self.btCalculate.setStyleSheet(u"QPushButton {\n"
"border: 3px solid black;\n"
"background-color: rgb(89, 255, 28);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 2px solid black;\n"
"background-color: rgb(89, 255, 28);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"border: 2px solid black;\n"
"background-color: rgb(13, 173, 26);\n"
"border-radius: 5px;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.btCalculate)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.listHearts = QListWidget(self.frame_2)
        self.listHearts.setObjectName(u"listHearts")
        self.listHearts.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHearts.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.listHearts)

        self.listDiamonds = QListWidget(self.frame_2)
        self.listDiamonds.setObjectName(u"listDiamonds")
        self.listDiamonds.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listDiamonds.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.listDiamonds)

        self.listSpades = QListWidget(self.frame_2)
        self.listSpades.setObjectName(u"listSpades")
        self.listSpades.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listSpades.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.listSpades)

        self.listClubs = QListWidget(self.frame_2)
        self.listClubs.setObjectName(u"listClubs")
        self.listClubs.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listClubs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.listClubs)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"High Card", None))
        self.l_highOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pair", None))
        self.l_pairOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Two Pair", None))
        self.l_twoPairOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Three of a Kind", None))
        self.l_ThreeOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Straight", None))
        self.l_straightOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Flush", None))
        self.l_flushOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Full House", None))
        self.l_fullOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Four of a Kind", None))
        self.l_fourOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Straight Flush", None))
        self.l_straightFlushOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Royal Flush", None))
        self.l_royalFlushOdd.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lbBoard1.setText("")
        self.lbBoard2.setText("")
        self.lbBoard3.setText("")
        self.lbBoard4.setText("")
        self.lbBoard5.setText("")
        self.lbHand1.setText("")
        self.lbHand2.setText("")
        self.btReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi


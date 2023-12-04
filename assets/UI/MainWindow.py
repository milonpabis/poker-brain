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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 600))
        self.centralwidget.setMaximumSize(QSize(1000, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
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
        self.frame_6.setStyleSheet(u"background-color: rgb(20, 223, 44);\n"
"background-color: rgb(66, 175, 27);\n"
"")
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
"background-color: rgb(66, 175, 27);")
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
        self.frame_4.setStyleSheet(u"background-color: rgb(66, 175, 27);")
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
        self.frame_5.setStyleSheet(u"background-color: rgb(66, 175, 27);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(250, 0, 250, 0)
        self.btCalculate = QPushButton(self.frame_5)
        self.btCalculate.setObjectName(u"btCalculate")
        self.btCalculate.setMinimumSize(QSize(200, 30))
        self.btCalculate.setMaximumSize(QSize(200, 30))
        font = QFont()
        font.setFamilies([u"Cooper Black"])
        font.setPointSize(16)
        self.btCalculate.setFont(font)
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

        self.verticalLayout_3.addWidget(self.btCalculate)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
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
        self.lbBoard1.setText("")
        self.lbBoard2.setText("")
        self.lbBoard3.setText("")
        self.lbBoard4.setText("")
        self.lbBoard5.setText("")
        self.lbHand1.setText("")
        self.lbHand2.setText("")
        self.btCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi


from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QListWidgetItem, QListWidget
from PySide6.QtCore import QMimeData, Qt, QByteArray, QDataStream, QIODevice, QPoint, QSize
from PySide6.QtGui import QPixmap, QDrag


class CardView(QLabel):

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        pixmap = QPixmap(f"images/{text}.png")
        self.value = text
        if pixmap.isNull():
            print("null")
        else:
            self.setPixmap(pixmap)
        self.setFixedHeight(120)
        self.setFixedWidth(80)
        self.setScaledContents(True)
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            drag.setMimeData(mime_data)
            drag.exec_(Qt.MoveAction)
    
    def sizeHint(self):
        return QSize(60, 80)

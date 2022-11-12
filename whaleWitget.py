from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap


class WhaleCont(QtWidgets.QWidget):
    def __init__(self, img, classes, *args, **kwargs):
        super(WhaleCont, self).__init__(*args, **kwargs)
        self.classes = classes
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.pixmap = QPixmap(img)
        self.label.mousePressEvent = self.selected
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selectedInit(self, *args, **kwargs):
        if self.selected:
            self.selected = False
        else:
            self.selected = True

    def deselect(self):
        self.label.setStyleSheet('border:1px solid black;')

    def select(self):
        self.label.setStyleSheet('border:3px solid cyan;')


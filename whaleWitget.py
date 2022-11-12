from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap


class WhaleCont(QtWidgets.QWidget):
    classes = ['/']
    jpg = '7ba843ae6b3493b63c4131499d34533f.jpg'
    def __init__(self, *args, **kwargs):
        super(WhaleCont, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.pixmap = QPixmap(self.jpg)
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

    def selected(self, *args, **kwargs):
        self.label.setText('Нажато')

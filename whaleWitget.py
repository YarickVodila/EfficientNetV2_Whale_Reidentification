from PyQt6 import QtCore, QtGui, QtWidgets


class WhaleCont(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(WhaleCont, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.mousePressEvent = self.selected

        self.label.setText('Ты пидор')
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

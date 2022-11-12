from PyQt6 import QtCore, QtGui, QtWidgets


class WhaleCont(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(WhaleCont, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setText('Ты пидор')
        layout.addWidget(self.label)
        self.setLayout(layout)

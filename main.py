from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from mainPage import Ui_MainWindow
import sys


class Whale(QMainWindow):
    def __init__(self):
        super(Whale,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Whale()
    window.show()
    sys.exit(app.exec())

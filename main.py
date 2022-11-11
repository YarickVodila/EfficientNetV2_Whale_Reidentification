from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from mainPage import Ui_MainWindow
from firstPage import Ui_IIntegrationWhale
import sys


class MainPageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainPageWindow = Ui_MainWindow()
        self.mainPageWindow.setupUi(self)


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.firstPageWindow = Ui_IIntegrationWhale()
        self.firstPageWindow.setupFirstPageUi(self)
        self.firstPageWindow.pushButton.clicked.connect(self.close)

    def close(self):
        self.mainPageWindow = MainPageWindow()
        self.mainPageWindow.show()
        self.hide()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstPage()
    window.show()
    sys.exit(app.exec())

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from mainPage import Ui_MainWindow
from firstPage import Ui_IIntegrationWhale
from whaleWitget import WhaleCont
import sys


class MainPageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainPageWindow = Ui_MainWindow()
        self.mainPageWindow.setupUi(self)
        self.mainPageWindow.BackButton.clicked.connect(self.back)
        self.createWhaleWitged()

    def back(self):
        self.firstPageWindow = FirstPage()
        self.firstPageWindow.show()
        self.hide()


    def createWhaleWitged(self):
        self.mainPageWindow.whaleWitged = WhaleCont(self.mainPageWindow.scrollAreaWidgetContents)
        print('sda')


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.firstPageWindow = Ui_IIntegrationWhale()
        self.firstPageWindow.setupUi(self)
        self.firstPageWindow.pushButton.clicked.connect(self.close)

    def close(self):
        self.mainPageWindow = MainPageWindow()
        self.mainPageWindow.show()
        self.hide()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open('./QSS-master/Aqua.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    window = FirstPage()
    window.show()
    sys.exit(app.exec())

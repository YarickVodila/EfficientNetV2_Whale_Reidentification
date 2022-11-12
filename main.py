import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QMainWindow

from firstPage import Ui_IIntegrationWhale
from mainPage import Ui_MainWindow
from whaleWitget import WhaleCont


class MainPageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainPageWindow = Ui_MainWindow()
        self.mainPageWindow.setupUi(self)
        self.mainPageWindow.BackButton.clicked.connect(self.back)
        self.createWhaleWitged("image.jpg")
        self.createWhaleWitged("7ba843ae6b3493b63c4131499d34533f.jpg")

    def back(self):
        self.firstPageWindow = FirstPage()
        self.firstPageWindow.show()
        self.hide()

    def createWhaleWitged(self, img):
        whaleWidget = WhaleCont(img)
        whaleWidget.setStyleSheet("background-color: rgb(77, 77, 77);")
        whaleWidget.label.mousePressEvent = partial(self.changeWhaleMainImage, whaleWidget)
        self.mainPageWindow.verticalLayout_2.addWidget(whaleWidget)

    def changeWhaleMainImage(self, whale, *args, **kwargs):
        self.mainPageWindow.label_3.setScaledContents(True)
        whale.selected()
        self.mainPageWindow.label_3.setPixmap(whale.pixmap)


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

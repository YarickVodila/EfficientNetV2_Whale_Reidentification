import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

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
        self.addTags()
        self.clearTags()

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


    def addTags(self, tags=None):
        if tags is None:
            tags = {'1': '1 Место по вироятности кита', '2': "2 Место по вироятности кита",'3': "3 Место по вироятности кита",'4': "4 Место по вироятности кита",'5': "5 Место по вироятности кита"}
        for i in tags:
            print(i)
            self.label = QLabel(self.mainPageWindow.frame_2)
            self.label.setText(tags[i])
            self.mainPageWindow.gridLayout_5.addWidget(self.label)


    def clearTags(self):
        for i in reversed(range(self.mainPageWindow.gridLayout_5.count())):
            self.mainPageWindow.gridLayout_5.itemAt(i).widget().deleteLater()



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

import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog

from firstPage import Ui_IIntegrationWhale
from mainPage import Ui_MainWindow
from whaleWitget import WhaleCont


class MainPageWindow(QMainWindow):
    def __init__(self, images):
        super().__init__()
        self.mainPageWindow = Ui_MainWindow()
        self.mainPageWindow.setupUi(self)
        self.mainPageWindow.BackButton.clicked.connect(self.back)
        for i in images:
            self.createWhaleWitged(i)

    def back(self):
        self.firstPageWindow = FirstPage()
        self.firstPageWindow.show()
        self.hide()

    def createWhaleWitged(self, img):
        whaleWidget = WhaleCont(img)
        whaleWidget.setStyleSheet("background-color: rgb(77, 77, 77); border-radius:0px; border:1px solid black")
        whaleWidget.label.mousePressEvent = partial(self.changeWhaleMain, whaleWidget)
        self.mainPageWindow.verticalLayout_2.addWidget(whaleWidget)

    def changeWhaleMain(self, whale, *args, **kwargs):
        self.mainPageWindow.label_3.setScaledContents(True)
        whale.selected()
        self.addTags(whale.classes)
        print(whale.classes)
        self.mainPageWindow.label_3.setPixmap(whale.pixmap)

    def addTags(self, tags=None):
        if tags is None:
            tags = {'1': '1 Место по вироятности кита', '2': "2 Место по вироятности кита",
                    '3': "3 Место по вироятности кита", '4': "4 Место по вироятности кита",
                    '5': "5 Место по вироятности кита"}
        for i in tags:
            self.label = QLabel(self.mainPageWindow.frame_2)
            self.label.setText(tags[i])
            self.label.setStyleSheet('border:None;')
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
        dlg = QFileDialog()
        # print(dlg.getOpenFileNames())
        fnames = QFileDialog.getOpenFileNames(self, 'Выбрать китов',
                                              None, "Киты (*.jpg *.png)")
        if len(fnames[0]) == 0:
            return
        self.mainPageWindow = MainPageWindow(fnames[0])
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

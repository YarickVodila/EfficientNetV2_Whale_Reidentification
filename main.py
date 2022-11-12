import sys
from functools import partial

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QWidget

import ml
from firstPage import Ui_IIntegrationWhale
from mainPage import Ui_MainWindow
from whaleWitget import WhaleCont


class MainPageWindow(QMainWindow):
    def __init__(self, images):
        super().__init__()
        self.mainPageWindow = Ui_MainWindow()
        self.mainPageWindow.setupUi(self)
        self.mainPageWindow.BackButton.clicked.connect(self.back)
        self.mainPageWindow.pushButton.clicked.connect(self.correctButtonInit)
        for img, top in images:
            self.createWhaleWidged(img, top)

    def back(self):
        self.firstPageWindow = FirstPage()
        self.firstPageWindow.show()
        self.hide()

    def createWhaleWidged(self, img, top):
        whaleWidget = WhaleCont(img, top)
        whaleWidget.setStyleSheet("background-color: rgb(77, 77, 77); border-radius:0px; border:1px solid black")
        whaleWidget.label.mousePressEvent = partial(self.changeWhaleMain, whaleWidget)
        self.mainPageWindow.verticalLayout_2.addWidget(whaleWidget)

    def deselect(self):
        items = (self.mainPageWindow.verticalLayout_2.itemAt(i) for i in
                 range(self.mainPageWindow.verticalLayout_2.count()))
        for w in items:
            w.widget().deselect()

    def changeWhaleMain(self, whale, *args, **kwargs):
        self.clearTags()
        self.mainPageWindow.label_3.setScaledContents(True)
        self.deselect()
        whale.select()
        self.addTags(whale.classes)
        self.mainPageWindow.label_3.setPixmap(whale.pixmap)

    def addTags(self, tags=None):
        if tags is None:
            tags = {'1': '1 Место по вироятности кита', '2': "2 Место по вироятности кита",
                    '3': "3 Место по вироятности кита", '4': "4 Место по вироятности кита",
                    '5': "5 Место по вироятности кита"}
        for i in tags:
            self.label = QLabel(self.mainPageWindow.frame_2)
            self.label.setText(str(i))
            self.label.setStyleSheet('border:None;')
            self.mainPageWindow.gridLayout_5.addWidget(self.label)

    def clearTags(self):
        for i in reversed(range(self.mainPageWindow.gridLayout_5.count())):
            self.mainPageWindow.gridLayout_5.itemAt(i).widget().deleteLater()

    def correctButtonInit(self):
        self.correctWindow = CorrectForm()


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.firstPageWindow = Ui_IIntegrationWhale()
        self.firstPageWindow.setupUi(self)
        self.firstPageWindow.pushButton.clicked.connect(self.close)

    def close(self):
        fnames = QFileDialog.getOpenFileNames(self, 'Выбрать китов',
                                              None, "Киты (*.jpg *.png)")
        if len(fnames[0]) == 0:
            return
        images = []
        self.firstPageWindow.progressBar.setRange(0, len(fnames[0]) + 1)
        for i, img in enumerate(fnames[0]):
            images.append((img, ml.get_top(img)))
            self.firstPageWindow.progressBar.setValue(i + 2)
        self.mainPageWindow = MainPageWindow(images)
        self.mainPageWindow.show()
        self.hide()


class CorrectForm(QWidget):
    def __init__(self):
        super(CorrectForm, self).__init__()  # Call the inherited classes __init__ method
        ui = uic.loadUi('correctForm.ui', self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open('./QSS-master/Aqua.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    window = FirstPage()
    window.show()
    sys.exit(app.exec())

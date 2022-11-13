import sys
from functools import partial
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QWidget

import ml
from first_page import Ui_IIntegrationWhale
from main_page import Ui_MainWindow
from whale_widget import WhaleCont


class MainPageWindow(QMainWindow):
    def __init__(self, images):
        super().__init__()
        self.main_page_window = Ui_MainWindow()
        self.main_page_window.setupUi(self)
        self.main_page_window.BackButton.clicked.connect(self.back)
        self.main_page_window.pushButton.clicked.connect(self.correct_button_init)
        for img, top in images:
            self.create_whale_widged(img, top)

    def back(self):
        self.first_page_window = FirstPage()
        self.first_page_window.show()
        self.hide()

    def create_whale_widged(self, img, top):
        whale_widget = WhaleCont(img, top)
        whale_widget.setStyleSheet("background-color: rgb(77, 77, 77); border-radius:0px; border:1px solid black")
        whale_widget.label.mousePressEvent = partial(self.change_whale_main, whale_widget)
        self.main_page_window.verticalLayout_2.addWidget(whale_widget)

    def deselect(self):
        items = (self.main_page_window.verticalLayout_2.itemAt(i) for i in
                 range(self.main_page_window.verticalLayout_2.count()))
        for w in items:
            w.widget().deselect()

    def change_whale_main(self, whale, *args, **kwargs):
        self.clear_ids()
        self.main_page_window.label_3.setScaledContents(True)
        self.deselect()
        whale.select()
        self.add_ids(whale.classes)
        self.main_page_window.label_3.setPixmap(whale.pixmap)

    def add_ids(self, ids):
        for i, id in enumerate(ids):
            self.label = QLabel(self.main_page_window.frame_2)
            self.label.setText(f"Топ {i+1}: {id}")
            self.label.setStyleSheet('border:None;')
            self.main_page_window.gridLayout_5.addWidget(self.label)

    def clear_ids(self):
        for i in reversed(range(self.main_page_window.gridLayout_5.count())):
            self.main_page_window.gridLayout_5.itemAt(i).widget().deleteLater()

    def correct_button_init(self):
        self.correct_window = CorrectForm()


class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.first_page_window = Ui_IIntegrationWhale()
        self.first_page_window.setupUi(self)
        self.first_page_window.pushButton.clicked.connect(self.close)

    def close(self):
        fnames = QFileDialog.getOpenFileNames(self, 'Выбрать китов',
                                              None, "Киты (*.jpg *.png)")
        if len(fnames[0]) == 0:
            return
        images = []
        self.first_page_window.progressBar.setRange(0, len(fnames[0]))
        for i, img in enumerate(fnames[0]):
            images.append((img, ml.get_top(img)))
            self.first_page_window.progressBar.setValue(i + 1)
        main_page_window = MainPageWindow(images)
        main_page_window.show()
        self.hide()


class CorrectForm(QWidget):
    def __init__(self):
        super(CorrectForm, self).__init__()
        path = Path(__file__).parent / "ui" / "correctForm.ui"
        ui = uic.loadUi(path, self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open(Path(__file__).parent / "ui" / "QSS-master" / "Aqua.qss", 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    window = FirstPage()
    window.show()
    sys.exit(app.exec())

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def applictation():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Кито`омайзер")
    window.setGeometry(800, 600, 800, 600)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    applictation()

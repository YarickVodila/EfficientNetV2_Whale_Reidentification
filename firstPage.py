# Form implementation generated from reading ui file 'FirstPageWhale.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_IIntegrationWhale(object):
    def setupUi(self, IIntegrationWhale):
        IIntegrationWhale.setObjectName("IIntegrationWhale")
        IIntegrationWhale.setEnabled(True)
        IIntegrationWhale.resize(800, 542)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IIntegrationWhale.sizePolicy().hasHeightForWidth())
        IIntegrationWhale.setSizePolicy(sizePolicy)
        IIntegrationWhale.setMinimumSize(QtCore.QSize(300, 150))
        IIntegrationWhale.setMaximumSize(QtCore.QSize(800, 542))
        IIntegrationWhale.setMouseTracking(False)
        IIntegrationWhale.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(IIntegrationWhale)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(270, 210, 250, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(63, 169, 245);\n"
"color: rgb(255, 255, 255);\n"
"font: 25 24pt \"Calibri Light\";\n"
"gridline-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(200, 310, 400, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(400, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 121, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/photo_2022-11-12_09-47-40.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        IIntegrationWhale.setCentralWidget(self.centralwidget)

        self.retranslateUi(IIntegrationWhale)
        QtCore.QMetaObject.connectSlotsByName(IIntegrationWhale)

    def retranslateUi(self, IIntegrationWhale):
        _translate = QtCore.QCoreApplication.translate
        IIntegrationWhale.setWindowTitle(_translate("IIntegrationWhale", "MainWindow"))
        self.pushButton.setText(_translate("IIntegrationWhale", "Выберите файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IIntegrationWhale = QtWidgets.QMainWindow()
    ui = Ui_IIntegrationWhale()
    ui.setupUi(IIntegrationWhale)
    IIntegrationWhale.show()
    sys.exit(app.exec())

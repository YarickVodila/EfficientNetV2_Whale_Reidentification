# Form implementation generated from reading ui file 'MainWorkWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 763)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftF = QtWidgets.QFrame(self.centralwidget)
        self.LeftF.setMaximumSize(QtCore.QSize(300, 16777215))
        self.LeftF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LeftF.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.LeftF.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.LeftF.setObjectName("LeftF")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LeftF)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ArchiveBox = QtWidgets.QGroupBox(self.LeftF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArchiveBox.sizePolicy().hasHeightForWidth())
        self.ArchiveBox.setSizePolicy(sizePolicy)
        self.ArchiveBox.setMinimumSize(QtCore.QSize(290, 301))
        self.ArchiveBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ArchiveBox.setFlat(False)
        self.ArchiveBox.setCheckable(False)
        self.ArchiveBox.setChecked(False)
        self.ArchiveBox.setObjectName("ArchiveBox")
        self.formLayout = QtWidgets.QFormLayout(self.ArchiveBox)
        self.formLayout.setObjectName("formLayout")
        self.widget = QtWidgets.QWidget(self.ArchiveBox)
        self.widget.setMinimumSize(QtCore.QSize(260, 656))
        self.widget.setMouseTracking(False)
        self.widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_2.setMouseTracking(True)
        self.widget_2.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_3.setMouseTracking(True)
        self.widget_3.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setMinimumSize(QtCore.QSize(100, 100))
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_4.setMouseTracking(True)
        self.widget_4.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setMinimumSize(QtCore.QSize(100, 100))
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_5.setMouseTracking(True)
        self.widget_5.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setMinimumSize(QtCore.QSize(100, 100))
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_5)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.ArchiveBox)
        self.verticalScrollBar.setGeometry(QtCore.QRect(259, 33, 16, 61))
        self.verticalScrollBar.setStyleSheet("background-color: rgb(110, 110, 110);")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalLayout_2.addWidget(self.ArchiveBox)
        self.horizontalLayout.addWidget(self.LeftF)
        self.CentralF = QtWidgets.QFrame(self.centralwidget)
        self.CentralF.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CentralF.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CentralF.setObjectName("CentralF")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CentralF)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.CentralF)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(500, 550))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.CentralF)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(500, 0))
        self.label_2.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.CentralF)
        self.Right = QtWidgets.QFrame(self.centralwidget)
        self.Right.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Right.setObjectName("Right")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Right)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BackButton = QtWidgets.QPushButton(self.Right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackButton.sizePolicy().hasHeightForWidth())
        self.BackButton.setSizePolicy(sizePolicy)
        self.BackButton.setMinimumSize(QtCore.QSize(70, 20))
        self.BackButton.setObjectName("BackButton")
        self.gridLayout_3.addWidget(self.BackButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.Right)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 3, 1)
        self.horizontalLayout.addWidget(self.Right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArchiveBox.setTitle(_translate("MainWindow", "Архив изображений"))
        self.label.setText(_translate("MainWindow", "Виджет с китом"))
        self.label_4.setText(_translate("MainWindow", "Виджет с китом"))
        self.label_5.setText(_translate("MainWindow", "Виджет с китом"))
        self.label_6.setText(_translate("MainWindow", "Виджет с китом"))
        self.label_3.setText(_translate("MainWindow", "Тут картинка с китами"))
        self.label_2.setText(_translate("MainWindow", "Тут набор тегов"))
        self.BackButton.setText(_translate("MainWindow", "Назад"))
        self.groupBox.setTitle(_translate("MainWindow", "Метаданные"))

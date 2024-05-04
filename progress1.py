from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget



class Ui_MainWindow(QWidget):
    def initUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/trish/Desktop/ADET/venv/icons/image.pmg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tracker_frame = QtWidgets.QFrame(Form)
        self.tracker_frame.setGeometry(QtCore.QRect(350, 10, 231, 231))
        self.tracker_frame.setStyleSheet("image: url(:/images/online-expensive-report-7042561-5727732-removebg-preview.png);\n"
"border: none;")
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.tracker_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tracker_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tracker_frame.setObjectName("tracker_frame")
        self.progressbar = QtWidgets.QFrame(Form)
        self.progressbar.setGeometry(QtCore.QRect(30, 250, 401, 131))
        self.progressbar.setStyleSheet("background-color: rgb(29, 29, 48);\n"
"border-radius: 20px;\n"
"border-bottom: 5px solid rgb(229, 170, 68);\n"
"border-right: 5px solid rgb(229, 170, 68);\n"
"border-top: 5px solid rgb(229, 170, 68);\n"
"border-left: 5px solid rgb(229, 170, 68);")
        self.progressbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progressbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progressbar.setObjectName("progressbar")
        self.progressBar = QtWidgets.QProgressBar(self.progressbar)
        self.progressBar.setGeometry(QtCore.QRect(30, 40, 351, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"border: 2px solid rgb(91, 214, 160);\n"
"text-align: center;\n"
"    font: 9pt \"Lucida Sans\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 93, 141, 255), stop:1 rgba(188, 122, 73, 255));\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.progressbar)
        self.label.setGeometry(QtCore.QRect(280, 20, 81, 16))
        self.label.setStyleSheet("border: none;\n"
"font: 75 italic 8pt \"MS Sans Serif\";\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.start = QtWidgets.QPushButton(self.progressbar)
        self.start.setGeometry(QtCore.QRect(150, 80, 93, 28))
        self.start.setStyleSheet("border: transparent;\n"
"background-color: rgb(230, 175, 74);\n"
"font: 87 8pt \"Arial Black\";\n"
"border-radius: 10px;")
        self.start.setObjectName("start")
        self.main_frame = QtWidgets.QFrame(Form)
        self.main_frame.setGeometry(QtCore.QRect(30, 80, 401, 181))
        self.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.095, y1:0.364364, x2:0.861, y2:0.573727, stop:0 rgba(195, 151, 226, 255), stop:1 rgba(29, 29, 48, 255));\n"
"border-radius: 20px;\n"
"border-bottom: 5px solid rgb(229, 170, 68);\n"
"border-right: 5px solid rgb(30, 29, 53);\n"
"border-top: 5px solid rgb(229, 170, 68);\n"
"border-left: 5px solid rgb(229, 170, 68);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.logo = QtWidgets.QFrame(self.main_frame)
        self.logo.setGeometry(QtCore.QRect(-90, -40, 291, 191))
        self.logo.setStyleSheet("image: url(:/images/Untitled_design__6_-removebg-preview.png);\n"
"background-color: none;\n"
"border: none; /*remove border*/")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.header_title = QtWidgets.QLabel(self.main_frame)
        self.header_title.setGeometry(QtCore.QRect(110, -50, 541, 201))
        self.header_title.setStyleSheet("border: none;\n"
"font: 75 25pt \"Verdana\";\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.header_title.setObjectName("header_title")
        self.header1_title = QtWidgets.QLabel(self.main_frame)
        self.header1_title.setGeometry(QtCore.QRect(130, 80, 211, 51))
        self.header1_title.setStyleSheet("border: none;\n"
"font: 75 25pt \"Verdana\";\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.header1_title.setObjectName("header1_title")
        self.label_2 = QtWidgets.QLabel(self.main_frame)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 281, 16))
        self.label_2.setStyleSheet("border: none;\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.trackerboarder_frame = QtWidgets.QFrame(Form)
        self.trackerboarder_frame.setGeometry(QtCore.QRect(350, 20, 241, 241))
        self.trackerboarder_frame.setStyleSheet("border: 5px solid rgb(229, 170, 68) ;\n"
"background-color: qlineargradient(spread:pad, x1:0.0248756, y1:0.886, x2:0.959876, y2:0.023, stop:0 rgba(29, 29, 48, 145), stop:1 rgba(229, 170, 68, 255));\n"
"border-radius: 20px;")
        self.trackerboarder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trackerboarder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trackerboarder_frame.setObjectName("trackerboarder_frame")
        self.trackerboarder_frame.raise_()
        self.progressbar.raise_()
        self.main_frame.raise_()
        self.tracker_frame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expense Tracker"))
        self.label.setText(_translate("Form", "Please wait..."))
        self.start.setText(_translate("Form", "START"))
        self.header_title.setText(_translate("Form", "EXPENSE"))
        self.header1_title.setText(_translate("Form", "TRACKER"))

import images_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 396)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("background-color: rgb(177, 174, 178);\n"
"color: rgb(240, 237, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(190, 320, 113, 32))
        self.nextButton.setStyleSheet("background-color: rgb(69, 117, 251);")
        self.nextButton.setObjectName("nextButton")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(60, 320, 113, 32))
        self.resetButton.setStyleSheet("background-color: rgb(69, 117, 251);")
        self.resetButton.setObjectName("resetButton")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(60, 250, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("#submitButton {\n"
"  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"}\n"
"\n"
"#submitButton:hover {background-color: #3e8e41}\n"
"\n"
"#submitButton:pressed {\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 20px;\n"
"min-width: 8em;\n"
"}\n"
"")
        self.submitButton.setCheckable(False)
        self.submitButton.setObjectName("submitButton")
        self.scoreboard = QtWidgets.QLCDNumber(self.centralwidget)
        self.scoreboard.setGeometry(QtCore.QRect(140, 10, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.scoreboard.setFont(font)
        self.scoreboard.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.scoreboard.setStyleSheet("background-color: rgb(73, 72, 74);\n"
"")
        self.scoreboard.setObjectName("scoreboard")
        self.answerBox = QtWidgets.QLineEdit(self.centralwidget)
        self.answerBox.setGeometry(QtCore.QRect(90, 200, 251, 21))
        self.answerBox.setStyleSheet("border: 1px solid black;\n"
"color: black;")
        self.answerBox.setObjectName("answerBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 200, 60, 21))
        self.label.setObjectName("label")
        self.quotesBox = QtWidgets.QLabel(self.centralwidget)
        self.quotesBox.setGeometry(QtCore.QRect(9, 80, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Telugu MN")
        font.setPointSize(14)
        self.quotesBox.setFont(font)
        self.quotesBox.setStyleSheet("color: black;")
        self.quotesBox.setAlignment(QtCore.Qt.AlignCenter)
        self.quotesBox.setWordWrap(True)
        self.quotesBox.setObjectName("quotesBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "ANSWER:"))
        self.quotesBox.setText(_translate("MainWindow", "Guess the movie based off the villain. Press Next to begin"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

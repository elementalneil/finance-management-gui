from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_MainWindow(object):
    def __init__(self):
        pass

    def setupUi(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainMenu()

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Finance Management"))
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def mainMenu(self):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainlabel = QtWidgets.QLabel(self.centralwidget)
        self.mainlabel.setGeometry(QtCore.QRect(70, 30, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Baron Neue")
        font.setPointSize(24)
        self.mainlabel.setFont(font)
        self.mainlabel.setObjectName("mainlabel")


        self.addMoneyBox = QtWidgets.QGroupBox(self.centralwidget)
        self.addMoneyBox.setGeometry(QtCore.QRect(100, 110, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addMoneyBox.setFont(font)
        self.addMoneyBox.setObjectName("addMoneyBox")

        self.addToSavings = QtWidgets.QRadioButton(self.addMoneyBox)
        self.addToSavings.setGeometry(QtCore.QRect(70, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addToSavings.setFont(font)
        self.addToSavings.setObjectName("addToSavings")

        self.addToWallet = QtWidgets.QRadioButton(self.addMoneyBox)
        self.addToWallet.setGeometry(QtCore.QRect(70, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addToWallet.setFont(font)
        self.addToWallet.setObjectName("addToWallet")

        self.addButton = QtWidgets.QPushButton(self.addMoneyBox)
        self.addButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.addButton.setObjectName("addButton")


        self.spendMoneyBox = QtWidgets.QGroupBox(self.centralwidget)
        self.spendMoneyBox.setGeometry(QtCore.QRect(100, 220, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spendMoneyBox.setFont(font)
        self.spendMoneyBox.setObjectName("spendMoneyBox")

        self.spendFromWallet = QtWidgets.QRadioButton(self.spendMoneyBox)
        self.spendFromWallet.setGeometry(QtCore.QRect(70, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spendFromWallet.setFont(font)
        self.spendFromWallet.setObjectName("spendFromWallet")

        self.spendFromSavings = QtWidgets.QRadioButton(self.spendMoneyBox)
        self.spendFromSavings.setGeometry(QtCore.QRect(70, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spendFromSavings.setFont(font)
        self.spendFromSavings.setObjectName("spendFromSavings")

        self.spendButton = QtWidgets.QPushButton(self.spendMoneyBox)
        self.spendButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.spendButton.setObjectName("spendButton")


        self.moveMoneyBox = QtWidgets.QGroupBox(self.centralwidget)
        self.moveMoneyBox.setGeometry(QtCore.QRect(100, 330, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.moveMoneyBox.setFont(font)
        self.moveMoneyBox.setObjectName("moveMoneyBox")

        self.moveToWallet = QtWidgets.QRadioButton(self.moveMoneyBox)
        self.moveToWallet.setGeometry(QtCore.QRect(70, 30, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.moveToWallet.setFont(font)
        self.moveToWallet.setObjectName("moveToWallet")

        self.moveToSavings = QtWidgets.QRadioButton(self.moveMoneyBox)
        self.moveToSavings.setGeometry(QtCore.QRect(70, 60, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.moveToSavings.setFont(font)
        self.moveToSavings.setObjectName("moveToSavings")

        self.moveButton = QtWidgets.QPushButton(self.moveMoneyBox)
        self.moveButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.moveButton.setObjectName("moveButton")


        self.MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.addMoneyBox.setTitle(_translate("MainWindow", "Add Money"))
        self.addToSavings.setText(_translate("MainWindow", "To Savings"))
        self.addToWallet.setText(_translate("MainWindow", "To Wallet"))
        self.addButton.setText(_translate("MainWindow", "Start Adding"))
        self.spendMoneyBox.setTitle(_translate("MainWindow", "Spend Money"))
        self.spendFromWallet.setText(_translate("MainWindow", "From Wallet"))
        self.spendFromSavings.setText(_translate("MainWindow", "From Savings"))
        self.spendButton.setText(_translate("MainWindow", "Start Spending"))
        self.moveMoneyBox.setTitle(_translate("MainWindow", "Move Money"))
        self.moveToWallet.setText(_translate("MainWindow", "From Savings to Wallet"))
        self.moveToSavings.setText(_translate("MainWindow", "From Wallet to Savings"))
        self.moveButton.setText(_translate("MainWindow", "Start Moving"))
        self.mainlabel.setText(_translate("MainWindow", "Main Menu"))

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.MainWindow.show()
    sys.exit(app.exec_())
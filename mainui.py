from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
import mainoperations
import sys

class Ui_MainWindow(object):
    def __init__(self, username):
        self.username=username
        print('Logged in as '+self.username)
        self.finances=mainoperations.financeoperations(self.username)

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
        self.addToSavings.clicked.connect(lambda: self.radioButtonChecker(self.addToSavings, self.addButton))

        self.addToWallet = QtWidgets.QRadioButton(self.addMoneyBox)
        self.addToWallet.setGeometry(QtCore.QRect(70, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addToWallet.setFont(font)
        self.addToWallet.setObjectName("addToWallet")
        self.addToWallet.clicked.connect(lambda: self.radioButtonChecker(self.addToWallet, self.addButton))

        self.addButton = QtWidgets.QPushButton(self.addMoneyBox)
        self.addButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(lambda: self.mainMenuPopup(self.addToWallet, self.addToSavings))


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
        self.spendFromWallet.clicked.connect(lambda: self.radioButtonChecker(self.spendFromWallet, self.spendButton))

        self.spendFromSavings = QtWidgets.QRadioButton(self.spendMoneyBox)
        self.spendFromSavings.setGeometry(QtCore.QRect(70, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spendFromSavings.setFont(font)
        self.spendFromSavings.setObjectName("spendFromSavings")
        self.spendFromSavings.clicked.connect(lambda: self.radioButtonChecker(self.spendFromSavings, self.spendButton))

        self.spendButton = QtWidgets.QPushButton(self.spendMoneyBox)
        self.spendButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.spendButton.setObjectName("spendButton")
        self.spendButton.clicked.connect(lambda: self.mainMenuPopup(self.spendFromWallet, self.spendFromSavings))

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
        self.moveToWallet.clicked.connect(lambda: self.radioButtonChecker(self.moveToWallet, self.moveButton))

        self.moveToSavings = QtWidgets.QRadioButton(self.moveMoneyBox)
        self.moveToSavings.setGeometry(QtCore.QRect(70, 60, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.moveToSavings.setFont(font)
        self.moveToSavings.setObjectName("moveToSavings")
        self.moveToSavings.clicked.connect(lambda: self.radioButtonChecker(self.moveToSavings, self.moveButton))

        self.moveButton = QtWidgets.QPushButton(self.moveMoneyBox)
        self.moveButton.setGeometry(QtCore.QRect(280, 32, 121, 41))
        self.moveButton.setObjectName("moveButton")
        self.moveButton.clicked.connect(lambda: self.mainMenuPopup(self.moveToWallet, self.moveToSavings))


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
        self.moveToWallet.setText(_translate("MainWindow", "Savings to Wallet"))
        self.moveToSavings.setText(_translate("MainWindow", "Wallet to Savings"))
        self.moveButton.setText(_translate("MainWindow", "Start Moving"))
        self.mainlabel.setText(_translate("MainWindow", "Main Menu"))

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def radioButtonChecker(self, radioButton, button):
        if button.text()=='Start Adding':
            action='add'
        elif button.text()=='Start Spending':
            action='spend'
        else:
            action='move'
        if radioButton.isChecked():
            if radioButton.text()=='To Savings' or radioButton.text()=='From Savings' or radioButton.text()=='Savings to Wallet':
                button.clicked.connect(lambda: self.mainMenuOptions(action, 's'))
            elif radioButton.text()=='To Wallet' or radioButton.text()=='From Wallet' or radioButton.text()=='Wallet to Savings':
                button.clicked.connect(lambda: self.mainMenuOptions(action, 'w'))

    def mainMenuPopup(self, radioButton1, radioButton2):
        if radioButton1.isChecked() or radioButton2.isChecked():
            return
        msg=QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText('Please Select an Account')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(msg.close)

        x=msg.exec_()

    def mainMenuOptions(self, action, account):
        if action=='add':
            if account=='s':
                self.addMenu('s')
            else:
                self.addMenu('w')
        elif action=='spend':
            if account=='s':
                self.spendMenu('s')
            else:
                self.spendMenu('w')
        else:
            if account=='s':
                self.moveMenu('s')
            else:
                self.moveMenu('w')

    def addMenu(self, account):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.headLabel = QtWidgets.QLabel(self.centralwidget)
        self.headLabel.setGeometry(QtCore.QRect(100, 30, 521, 61))
        font = QtGui.QFont()
        font.setFamily("Baron Neue")
        font.setPointSize(28)
        self.headLabel.setFont(font)
        self.headLabel.setObjectName("headLabel")

        self.sBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.sBalLabel.setGeometry(QtCore.QRect(50, 120, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sBalLabel.setFont(font)
        self.sBalLabel.setObjectName("sBalLabel")

        self.wBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.wBalLabel.setGeometry(QtCore.QRect(50, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wBalLabel.setFont(font)
        self.wBalLabel.setObjectName("wBalLabel")

        self.getAmtLabel = QtWidgets.QLabel(self.centralwidget)
        self.getAmtLabel.setGeometry(QtCore.QRect(110, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmtLabel.setFont(font)
        self.getAmtLabel.setObjectName("getAmtLabel")

        self.getAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.getAmount.setGeometry(QtCore.QRect(330, 215, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmount.setFont(font)
        self.getAmount.setValidator(QIntValidator(0,2147483647))
        self.getAmount.setObjectName("getAmount")

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(140, 270, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(lambda:self.addAction(account, self.getAmount.text(), self.sBalLabel, self.wBalLabel))

        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(170, 410, 101, 31))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.mainMenuButton.clicked.connect(self.mainMenu)

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(350, 410, 101, 31))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.closeAction)  


        self.MainWindow.setCentralWidget(self.centralwidget)       

        _translate = QtCore.QCoreApplication.translate

        if account=='w':
            self.headLabel.setText(_translate("MainWindow", "add money to wallet"))
        else:
            self.headLabel.setText(_translate("MainWindow", "add money to savings"))

        self.sBalLabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        self.wBalLabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmtLabel.setText(_translate("MainWindow", "Enter the Amount to Add:"))
        self.addButton.setText(_translate("MainWindow", "Add Money"))
        self.mainMenuButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.mainMenuButton.setShortcut(_translate("MainWindow", "Escape"))
        self.closeButton.setText(_translate("MainWindow", "Close"))

    def addAction(self, account, amount, slabel, wlabel):
        self.successPopup()
        self.finances.addMoney(account, int(amount))
        slabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        wlabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmount.setText('')

    def closeAction(self):
        self.MainWindow.close()

    def spendMenu(self, account):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.headLabel = QtWidgets.QLabel(self.centralwidget)
        self.headLabel.setGeometry(QtCore.QRect(63, 30, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Baron Neue")
        font.setPointSize(26)
        self.headLabel.setFont(font)
        self.headLabel.setObjectName("headLabel")

        self.sBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.sBalLabel.setGeometry(QtCore.QRect(50, 120, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sBalLabel.setFont(font)
        self.sBalLabel.setObjectName("sBalLabel")

        self.wBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.wBalLabel.setGeometry(QtCore.QRect(50, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wBalLabel.setFont(font)
        self.wBalLabel.setObjectName("wBalLabel")

        self.getAmtLabel = QtWidgets.QLabel(self.centralwidget)
        self.getAmtLabel.setGeometry(QtCore.QRect(110, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmtLabel.setFont(font)
        self.getAmtLabel.setObjectName("getAmtLabel")

        self.getAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.getAmount.setGeometry(QtCore.QRect(330, 215, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmount.setFont(font)
        if account=='w':
            self.getAmount.setValidator(QIntValidator(1, self.finances.walletBalance))
        else:
            self.getAmount.setValidator(QIntValidator(1, self.finances.savingsBalance))
        self.getAmount.setObjectName("getAmount")

        self.spendButton = QtWidgets.QPushButton(self.centralwidget)
        self.spendButton.setGeometry(QtCore.QRect(140, 270, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spendButton.setFont(font)
        self.spendButton.setObjectName("spendButton")
        self.spendButton.clicked.connect(lambda:self.spendAction(account, self.getAmount.text(), self.sBalLabel, self.wBalLabel))

        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(170, 410, 101, 31))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.mainMenuButton.clicked.connect(self.mainMenu)

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(350, 410, 101, 31))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.closeAction)


        self.MainWindow.setCentralWidget(self.centralwidget)       

        _translate = QtCore.QCoreApplication.translate

        if account=='w':
            self.headLabel.setText(_translate("MainWindow", "spend money from wallet"))
        else:
            self.headLabel.setText(_translate("MainWindow", "spend money from savings"))

        self.sBalLabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        self.wBalLabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmtLabel.setText(_translate("MainWindow", "Enter the Amount to Spend:"))
        self.spendButton.setText(_translate("MainWindow", "Spend Money"))
        self.mainMenuButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.mainMenuButton.setShortcut(_translate("MainWindow", "Escape"))
        self.closeButton.setText(_translate("MainWindow", "Close"))

    def spendAction(self, account, amount, slabel, wlabel):
        if amount=='':
            return

        if account=='s':
            if self.finances.savingsBalance<int(amount):
                self.insufficientPopup()
                self.getAmount.setText('')
                return
        else:
            if self.finances.walletBalance<int(amount):
                self.insufficientPopup()
                self.getAmount.setText('')
                return

        self.successPopup()
        self.finances.spendMoney(account, int(amount))
        slabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        wlabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmount.setText('')

    def insufficientPopup(self):
        msg=QMessageBox()
        msg.setWindowTitle('Warning')
        msg.setText('Insufficient Funds')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(msg.close)

        x=msg.exec_()

    def successPopup(self):
        msg=QMessageBox()
        msg.setWindowTitle('Success')
        msg.setText('Transaction Successful!')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(msg.close)

        x=msg.exec_()

    def moveMenu(self, account):
        self.centralwidget.deleteLater()
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.headLabel = QtWidgets.QLabel(self.centralwidget)
        self.headLabel.setGeometry(QtCore.QRect(150, 30, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Baron Neue")
        font.setPointSize(26)
        self.headLabel.setFont(font)
        self.headLabel.setObjectName("headLabel")

        self.sBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.sBalLabel.setGeometry(QtCore.QRect(50, 120, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sBalLabel.setFont(font)
        self.sBalLabel.setObjectName("sBalLabel")

        self.wBalLabel = QtWidgets.QLabel(self.centralwidget)
        self.wBalLabel.setGeometry(QtCore.QRect(50, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wBalLabel.setFont(font)
        self.wBalLabel.setObjectName("wBalLabel")

        self.getAmtLabel = QtWidgets.QLabel(self.centralwidget)
        self.getAmtLabel.setGeometry(QtCore.QRect(110, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmtLabel.setFont(font)
        self.getAmtLabel.setObjectName("getAmtLabel")

        self.getAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.getAmount.setGeometry(QtCore.QRect(330, 215, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAmount.setFont(font)
        if account=='w':
            self.getAmount.setValidator(QIntValidator(1, self.finances.walletBalance))
        else:
            self.getAmount.setValidator(QIntValidator(1, self.finances.savingsBalance))
        self.getAmount.setObjectName("getAmount")

        self.moveButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveButton.setGeometry(QtCore.QRect(140, 270, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moveButton.setFont(font)
        self.moveButton.setObjectName("moveButton")
        self.moveButton.clicked.connect(lambda:self.moveAction(account, self.getAmount.text(), self.sBalLabel, self.wBalLabel))

        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(170, 410, 101, 31))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.mainMenuButton.clicked.connect(self.mainMenu)

        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(350, 410, 101, 31))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(self.closeAction)


        self.MainWindow.setCentralWidget(self.centralwidget)       

        _translate = QtCore.QCoreApplication.translate

        if account=='s':
            self.headLabel.setText(_translate("MainWindow", "savings to wallet"))
        else:
            self.headLabel.setText(_translate("MainWindow", "wallet to savings"))

        self.sBalLabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        self.wBalLabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmtLabel.setText(_translate("MainWindow", "Enter the Amount to Move:"))
        self.moveButton.setText(_translate("MainWindow", "Move Money"))
        self.mainMenuButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.mainMenuButton.setShortcut(_translate("MainWindow", "Escape"))
        self.closeButton.setText(_translate("MainWindow", "Close"))

    def moveAction(self, account, amount, slabel, wlabel):
        if amount=='':
            return

        if account=='s':
            if self.finances.savingsBalance<int(amount):
                self.insufficientPopup()
                self.getAmount.setText('')
                return
        else:
            if self.finances.walletBalance<int(amount):
                self.insufficientPopup()
                self.getAmount.setText('')
                return

        if amount=='':
            return

        self.successPopup()
        self.finances.moveMoney(account, int(amount))
        slabel.setText('Savings Balance: '+str(self.finances.savingsBalance))
        wlabel.setText('Wallet Balance: '+str(self.finances.walletBalance))
        self.getAmount.setText('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.MainWindow.show()
    sys.exit(app.exec_())
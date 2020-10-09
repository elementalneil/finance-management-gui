from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import db
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.newportal = db.portal()

    def setupUi(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginui()

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login System"))

    def loginui(self):
        self.clearLayout(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.inputUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsername.setGeometry(QtCore.QRect(280, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputUsername.setFont(font)
        self.inputUsername.setObjectName("inputUsername")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(280, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputPassword.setFont(font)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(220, 300, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.loginButton.setPalette(palette)
        self.loginButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.loginButton.setObjectName("loginButton")

        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(250, 380, 131, 31))
        self.signupButton.setObjectName("signupButton")

        self.MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Log in to Your Account"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.signupButton.setText(_translate("MainWindow", "Signup Instead..."))

        self.loginButton.clicked.connect(lambda: self.getloginfields(self.inputUsername.text(), self.inputPassword.text()))
        self.signupButton.clicked.connect(self.signupui)

    def getloginfields(self, username, password):
        status=self.newportal.login(username, password)
        if username=='' or password=='':
            self.login_error_popup('empty')
        elif(status==1):
            self.login_error_popup('un')
        elif(status==2):
            self.login_error_popup('pw')
        elif(status==3):
            self.showstatus(username)

    def login_error_popup(self, errortype):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        if errortype=='empty':
            msg.setText('Incomplete Credentials!')
            msg.setInformativeText('The fields entered cannot be empty. Please try again.')
        elif errortype=='un':
            msg.setText('Wrong Username!')
            msg.setInformativeText('The username entered does not exist. Please try again.')
        else:
            msg.setText('Wrong Password!')
            msg.setInformativeText('The password does not match. Please try again.')
        msg.setWindowTitle('Error')
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.login_error_popup_actions)

        x=msg.exec_()

    def login_error_popup_actions(self, option):
        if option.text()=='OK':
            self.loginui()
        else:
            self.MainWindow.close()

    def signupui(self):
        self.clearLayout(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.inputUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsername.setGeometry(QtCore.QRect(310, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputUsername.setFont(font)
        self.inputUsername.setObjectName("inputUsername")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setGeometry(QtCore.QRect(310, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputPassword.setFont(font)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.inputPassword2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword2.setGeometry(QtCore.QRect(310, 270, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputPassword2.setFont(font)
        self.inputPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword2.setObjectName("inputPassword2")

        self.signupButton = QtWidgets.QPushButton(self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(220, 340, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.signupButton.setPalette(palette)
        self.signupButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.signupButton.setObjectName("signupButton")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(250, 410, 131, 31))
        self.loginButton.setObjectName("loginButton")

        self.MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Create New Account"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Confirm Password"))
        self.signupButton.setText(_translate("MainWindow", "SIGN UP"))
        self.loginButton.setText(_translate("MainWindow", "Login Instead..."))

        self.signupButton.clicked.connect(lambda: self.getsignupfields(self.inputUsername.text(), self.inputPassword.text(), self.inputPassword2.text()))
        self.loginButton.clicked.connect(self.loginui)

    def getsignupfields(self, username, password1, password2):
        if password1!=password2:
            self.signup_error_popup('pw')
        elif username=='' or password1=='' or password2=='':
            self.signup_error_popup('empty')
        else:
            if self.newportal.signup(username, password1):
                self.signup_success_popup(username)
            else:
                self.signup_error_popup('un')

    def signup_success_popup(self, username):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Signup Successful!')
        msg.setInformativeText('Welcome '+username+'. Your account is created. Please login to continue.')
        msg.setWindowTitle('Success')
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.signup_success_popup_actions)

        x=msg.exec_()

    def signup_success_popup_actions(self, option):
        if option.text()=='OK':
            self.loginui()
        else:
            self.MainWindow.close()

    def signup_error_popup(self, errortype):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        if errortype=='pw':
            msg.setText('Passwords do not match!')
            msg.setInformativeText('Both passwords should be the same. Please try again.')
        elif errortype=='empty':
            msg.setText('Incomplete Credentials!')
            msg.setInformativeText('The fields entered cannot be empty. Please try again.')
        else:
            msg.setText('Username Taken!')
            msg.setInformativeText('The username you entered is taken. Please try another.')
        msg.setWindowTitle('Error')
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.signup_error_popup_actions)

        x=msg.exec_()

    def signup_error_popup_actions(self, option):
        if option.text()=='OK':
            self.signupui()
        else:
            self.MainWindow.close()

    def showstatus(self, username):
        self.clearLayout(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("You're logged in as "+username)
        self.MainWindow.setCentralWidget(self.centralwidget)

    def clearLayout(self, layout):
        layout.deleteLater()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.MainWindow.show()
    sys.exit(app.exec_())
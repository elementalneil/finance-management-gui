import mainui
import loginui
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
ui = loginui.Ui_MainWindow()
ui.setupUi()
ui.MainWindow.show()
app.exec_()

username=ui.username
# print('Logged in as '+username)

app2 = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
ui2 = mainui.Ui_MainWindow(username)
ui2.setupUi()
ui2.MainWindow.show()
app2.exec_()

sys.exit()
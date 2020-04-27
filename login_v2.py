#porthub file
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from singup import signUp_Dialog
from welcome import Ui_MainWindow


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 435)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.uname_label = QtWidgets.QLabel(Dialog)
        self.uname_label.setGeometry(QtCore.QRect(220, 220, 91, 51))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.uname_label.setFont(font)
        self.uname_label.setStyleSheet("color: rgb(221, 147, 0);")
        self.uname_label.setObjectName("uname_label")

        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(220, 260, 91, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(221, 147, 0);")
        self.pass_label.setObjectName("pass_label")

        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(330, 230, 211, 25))
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(330, 270, 211, 25))
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.login_Button = QtWidgets.QPushButton(Dialog)
        self.login_Button.setGeometry(QtCore.QRect(340, 310, 89, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_Button.setFont(font)
        self.login_Button.setStyleSheet("color: rgb(221, 147, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.login_Button.setObjectName("login_Button")

        self.signUp_Button = QtWidgets.QPushButton(Dialog)
        self.signUp_Button.setGeometry(QtCore.QRect(450, 310, 89, 25))
        self.signUp_Button.setStyleSheet("color: rgb(221, 147, 0);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signUp_Button.setFont(font)
        self.signUp_Button.setObjectName("signUp_Button")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 70, 591, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.login_Button.clicked.connect(self.loginCheck)
        self.signUp_Button.clicked.connect(self.signUpCheck)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome to PortHub!"))
        self.uname_label.setText(_translate("Dialog", "USERNAME"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_Button.setText(_translate("Dialog", "Login"))
        self.signUp_Button.setText(_translate("Dialog", "Sign Up"))

    def signUpShow(self): #this connects the sign up button to the sign up window
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = signUp_Dialog()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

    def welcomeWindowShow(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    

    def loginCheck(self):
        username = self.username_lineEdit.text() #gets text from the username line edit widget
        password = self.password_lineEdit.text() #gets text from the password line edit widget

        connection = sqlite3.connect("porthub.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        
        if(len(result.fetchall()) > 0):
            print("User found!")
            #this function redirects user to the main window after a successful login
            self.welcomeWindowShow()
            
        else:
            print("User not found")
            self.showMessageBox("Warning", "Invalid Username and/or Password")

    def signUpCheck(self):
        self.signUpShow()
    
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


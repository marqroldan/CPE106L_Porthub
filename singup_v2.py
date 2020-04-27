#porthub file 
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class signUp_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 651)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
####################################################################################
        #Labels section
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 320, 101, 17))
        self.label.setStyleSheet("color: rgb(221, 147, 0);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 450, 101, 17))
        self.label_2.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 380, 101, 17))
        self.label_3.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_3.setObjectName("label_3")
    
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 180, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 50, 591, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(410, 320, 101, 17))
        self.label_6.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(410, 450, 101, 17))
        self.label_7.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(410, 500, 101, 17))
        self.label_8.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 500, 101, 17))
        self.label_9.setStyleSheet("color: rgb(221, 147, 0);")
        self.label_9.setObjectName("label_9")

############################################################################################
        #line edits section
        self.firstName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.firstName_lineEdit.setGeometry(QtCore.QRect(200, 320, 171, 25))
        self.firstName_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.firstName_lineEdit.setObjectName("firstName_lineEdit")

        self.address_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.address_lineEdit.setGeometry(QtCore.QRect(200, 380, 541, 25))
        self.address_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.address_lineEdit.setObjectName("address_lineEdit")

        self.username_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(200, 450, 171, 25))
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.lastName_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lastName_lineEdit.setGeometry(QtCore.QRect(570, 320, 171, 25))
        self.lastName_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lastName_lineEdit.setObjectName("lastName_lineEdit")

        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(570, 450, 171, 25))
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.contactNumber_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.contactNumber_lineEdit.setGeometry(QtCore.QRect(570, 500, 171, 25))
        self.contactNumber_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contactNumber_lineEdit.setObjectName("contactNumber_lineEdit")

        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(200, 500, 171, 25))
        self.email_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_lineEdit.setObjectName("email_lineEdit")

####################################################################################################
        
        #buttons section
        self.signUp_button = QtWidgets.QPushButton(Dialog)
        self.signUp_button.setGeometry(QtCore.QRect(330, 550, 89, 25))
        self.signUp_button.setStyleSheet("color: rgb(221, 147, 0);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signUp_button.setFont(font)
        self.signUp_button.setObjectName("signUp_button")
        self.signUp_button.clicked.connect(self.signUpClick)
    



        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Welcome to PortHub!"))
        self.label.setText(_translate("Dialog", "FIRST NAME"))
        self.label_2.setText(_translate("Dialog", "USERNAME"))
        self.label_3.setText(_translate("Dialog", "ADDRESS"))
        self.signUp_button.setText(_translate("Dialog", "Sign Up"))
        self.label_4.setText(_translate("Dialog", "Create Account"))
        self.label_6.setText(_translate("Dialog", "LAST NAME"))
        self.label_7.setText(_translate("Dialog", "PASSWORD"))
        self.label_8.setText(_translate("Dialog", "CONTACT NO."))
        self.label_9.setText(_translate("Dialog", "E-MAIL ADDRESS"))


    ############################################################################################

    #function for the code
    def signUpClick(self):
        fName = self.firstName_lineEdit.text()
        lName = self.lastName_lineEdit.text()
        address = self.address_lineEdit.text()
        contactNumber = self.contactNumber_lineEdit.text()
        username = self.username_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()

        #this is the order on how to insert values 
        #FNAME, LNAME, USER_ADDRESS, USERNAME, PASSWORD, EMAIL, CONTACT_NUMBER

        connection = sqlite3.connect("porthub.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?)",(fName,lName,address,username,password,email,contactNumber))
        connection.commit()
        connection.close()
        self.showMessageBox("Sign Up Successful","Your information has been added to the database")

        self.firstName_lineEdit.clear()
        self.lastName_lineEdit.clear()
        self.address_lineEdit.clear()
        self.contactNumber_lineEdit.clear()
        self.username_lineEdit.clear()
        self.email_lineEdit.clear()
        self.password_lineEdit.clear()


        


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
    ui = signUp_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


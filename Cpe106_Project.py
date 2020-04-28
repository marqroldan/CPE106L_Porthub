import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from article import Ui_ArticleWindow
from main import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

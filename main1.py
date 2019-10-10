from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLineEdit, QLabel, QDialog, QMessageBox
import sys
from PyQt5 import QtGui, QtCore
import reset_pass
import MainPage
import Dialog
import MySQLdb as mdb

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "HBADS"
        left = 500
        top = 200
        width = 500
        height = 300
        iconName = "cctv"


        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle(title)
        self.setGeometry(left,top,width,height)

        self.UIcomponent()



        self.show()
    def abc(self):
        #self.showDialog()
        #print("Welcome")
        try:
            connection = mdb.connect('localhost','root','','hbads')
            #self.showDialog("CONNECTED")
            Query = "select username,password from login"
            cursor = connection.cursor()
            cursor.execute(Query)
            records = cursor.fetchall()
            u = self.username.text()
            v = self.password.text()
            for row in records:
                #print("Id = ", row[0], )
                #print("Name = ", row[1], "\n")
                if u == row[0] and v == row[1]:
                    #print("Zeeshan")
                    Dialog.message("Welcome","Logged In Sucessfully!")
                    self.main_lib = MainPage.PageMain()
                    self.main_lib.show()
                    self.hide()
                #print("Price  = ", row[2], "\n")
                #print("Purchase date  = ", row[3], "\n")
        except mdb.Error as e:
            self.showDialog(e)
            sys.exit()
       # finally:
            #if (connection.is_connected()):
                #connection.close()
                #cursor.close()
                #print("MySQL connection is closed")

        #self.main_lib = MainPage.PageMain()
        #self.main_lib.show()
        #self.hide()

    def bcd(self):

        print("Welcome")
        self.new_lib = reset_pass.WindowA()
        self.new_lib.show()
        self.hide()

    def UIcomponent(self):
      #  hbox = QHBoxLayout()
        labelimg = QLabel(self)
        pixmap = QPixmap("lock.png")
        pixmap.setDevicePixelRatio(8)
        labelimg.setPixmap(pixmap)
        labelimg.setGeometry(QRect(170, 1, 50, 60))
        self.label = QLabel(self)
        self.label.setText("LOGIN")
        self.label.setFont(QtGui.QFont("Sanserif", 18, weight=QtGui.QFont.Bold))
        self.label.setGeometry(QRect(225, 25, 250, 28))
        #self.label = QLabel(self)
        #self.label.setGeometry(QRect(160, 0, 150, 100))



        self.login_button = QPushButton("",self)
        self.login_button.setGeometry(QRect(185,190,140,38))
        self.login_button.setIcon(QtGui.QIcon("Login.png"))
        self.login_button.setIconSize(QtCore.QSize(161,55))
        self.login_button.clicked.connect(self.abc)


        self.username = QLineEdit(self)
        self.username.setFont(QtGui.QFont("Sanserif", 11))
        self.username.setText("s")
        self.username.setGeometry(QRect(160, 100, 250, 28))

        self.password = QLineEdit(self)
        self.password.setFont(QtGui.QFont("Sanserif", 11))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setText("s")
        self.password.setGeometry(QRect(160, 140, 250, 28))

        self.label1 = QLabel(self)
        self.label1.setText("Username")
        self.label1.setFont(QtGui.QFont("Sanserif", 15,weight=QtGui.QFont.Bold))
        self.label1.setGeometry(QRect(30, 90, 250, 28))

        self.label2 = QLabel(self)
        self.label2.setText("Password")
        self.label2.setFont(QtGui.QFont("Sanserif", 15, weight=QtGui.QFont.Bold))
        self.label2.setGeometry(QRect(30, 140, 250, 28))



        self.label3 = QPushButton(self)
        self.label3.setText("Foregot Username/Password?")
        self.label3.setFont(QtGui.QFont("Sanserif", 12, weight=QtGui.QFont.Bold))
        self.label3.setStyleSheet("color : blue")
        self.label3.setGeometry(QRect(230, 265, 255, 27))
        self.label3.clicked.connect(self.bcd)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
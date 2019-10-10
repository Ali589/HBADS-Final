from PyQt5.QtCore import QRect, QSize, pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLineEdit, QLabel, QComboBox, QWidget, \
    QCheckBox, QRadioButton, QGroupBox, QGridLayout, QDialog, QVBoxLayout, QFrame, QMessageBox
import sys
from PyQt5 import QtGui, QtCore
import main1


class WindowA(QWidget):
    def __init__(self, title="Reset Settings"):
        super().__init__()  # inherit init of QWidget
        self.title = title
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 250
        self.iconName = "cctv"
        self.widget()
        self.show()

    def widget(self):
        # window setup
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        ## use above line or below
        self.resize(self.width, self.height)
        self.move(self.left, self.top)

        self.emlab = QLabel(self)
        self.emlab.setText("Enter Your Email")
        self.emlab.setFont(QtGui.QFont("Sanserif", 15, weight=QtGui.QFont.Bold))
        self.emlab.setGeometry(QRect(30, 50, 250, 28))

        self.em = QLineEdit(self)
        self.em.setFont(QtGui.QFont("Sanserif", 11))
        self.em.setGeometry(QRect(30, 90, 400, 28))


        # create frame for a set of checkbox
        self.frame1 = QFrame(self)
        self.frame1.setGeometry(QRect(30, 150, 470, 50))
        #self.frame1.move(40, 40)

        self.checkbox1 = QCheckBox("Send My Username", self.frame1)
        self.checkbox1.move(0, 0)
        self.checkbox2 = QCheckBox("Send new Password", self.frame1)
        self.checkbox2.setChecked(True)
        self.checkbox2.move(0, 20)

        # push button to display output on label
        self.btn1 = QPushButton(self.frame1, text="Submit")
        self.btn1.move(220, 20)
        self.btn1.clicked.connect(self.reset_method)


        self.btn2 = QPushButton(self.frame1, text="Back")
        self.btn2.move(320, 20)
        self.btn2.clicked.connect(self.back_method)


        # selected value will be displayed on label
        self.emlab = QLabel(self.frame1)
        self.emlab.setGeometry(QRect(60, 0, 500, 20))
        # self.label1.move(60, 0)




    def back_method(self):
        self.prev_lib = main1.Window()
        self.prev_lib.show()
        self.hide()
    def reset_method(self):
        self.showDialog("Information","Settings Applied Sucessfully!")
        print("Password is set")
        sys.exit()


    def showDialog(self,head,text):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(head)
        msgBox.setStandardButtons(QMessageBox.Ok)
        #msgBox.buttonClicked.connect(msgButtonClick(a))
        returnValue = msgBox.exec()
        #if returnValue == QMessageBox.Ok:
         #   print('OK clicked')

import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QRect
import MySQLdb as mdb
import ast


def MyConverter(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt, mydata))

class App(QWidget):

    def LoadData(self):
        connection = mdb.connect('localhost', 'root', '', 'hbads')
        Query = "SELECT * FROM REPORTING ORDER BY DATETIME DESC"
        cursor = connection.cursor()
        cursor.execute(Query)
        records = cursor.fetchall()

        for row in records:
            self.AddTable(MyConverter(row))
        cursor.close()

    def AddTable(self,cols):
        row_pos = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_pos)

        for i,column in enumerate(cols):
            self.tableWidget.setItem(row_pos, i , QtWidgets.QTableWidgetItem(column))

    def __init__(self):
        super().__init__()
        self.title = 'HBADS'
        self.left = 0
        self.top = 0
        self.width = 1366
        self.height = 768
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("cctv.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.setGeometry(QRect(self.left, self.top, self.width,self. height))
        self.setLayout(self.layout)
        # Show widget
        self.LoadData()
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.move(0, 0)
        self.tableWidget.setHorizontalHeaderLabels(["S.No","Anomaly Name","Anomaly Type","Date/Time"])
        vheader = self.tableWidget.verticalHeader()
        vheader.setVisible(False)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


#if __name__ == '__main__':
 #   app = QApplication(sys.argv)
 #   ex = App()
 #   sys.exit(app.exec_())
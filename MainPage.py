import cv2
from PyQt5.QtCore import QRect, Qt, QTimer, QThreadPool
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLineEdit, QLabel, QDialog, \
    QMessageBox, QFrame, QCheckBox, QGroupBox, QVBoxLayout, QWidget, QSplitter, QGraphicsScene, QGraphicsView, \
    QGridLayout, QSlider
import sys
import numpy as np
import MySQLdb as mdb
from PyQt5 import QtGui, QtCore
import ReportAnom
import Dialog
import DispSettings
import main1


class PageMain(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.a = False
        self.title = "HBADS"
        self.left = 0
        self.top = 0
        self.width = 1366
        self.height = 768
        self.iconName = "cctv"
        self.initWindow()

    def initWindow(self):

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setFixedWidth(1366)
        self.setFixedHeight(768)
        self.setWindowTitle(self.title)
       # self.setGeometry(self.left, self.top, self.width, self.height)


      #  self.show()
        hbox = QHBoxLayout(self)

        splitter1 = QSplitter(self)
        splitter1.setOrientation(Qt.Horizontal)

        left = QFrame(splitter1)
        left.setGeometry(0, 0, 20, 768)
        left.setFixedWidth(200)
        left.setStyleSheet("background-color:white")
        left.setFrameShape(QFrame.StyledPanel)

        self.wall = QFrame(splitter1)
        self.wall.setFrameShape(QFrame.StyledPanel)

        self.center = QFrame(splitter1)
        self.center.setFrameShape(QFrame.StyledPanel)

        self.sett = QFrame(splitter1)
        self.sett.setFrameShape(QFrame.StyledPanel)

        hbox.addWidget(splitter1)
        self.setGeometry(self.left, self.top, 910, 550)

        self.image_label = QLabel("",self.center)
        #self.image_label.setStyleSheet("background-color:blue")
        self.image_label.setGeometry(QRect(0,0,1200,700))

        self.reporting_label = QLabel("", self.center)
        # self.image_label.setStyleSheet("background-color:blue")
        self.reporting_label.setGeometry(QRect(0, 0, 1200, 700))

        #### For Main Wall
        self.welcome = QLabel("Welcome to Human Body Anomaly Detection System",self.wall)
        self.welcome.setGeometry(0,0,1200,700)
        self.welcome.setStyleSheet("font-size:20px; font-weight:bold")
        ###FOR MENU BUTTONS
        self.btn1 = QPushButton("",left)
        self.btn1.setGeometry(15,21,170,40)
        self.btn1.setIcon(QtGui.QIcon("Cameras.png"))
        self.btn1.setIconSize(QtCore.QSize(240, 65))
        self.btn1.clicked.connect(self.cam_click)


        self.btn2 = QPushButton("", left)
        self.btn2.setGeometry(15, 64, 170, 40)
        self.btn2.setIcon(QtGui.QIcon("Reporting.png"))
        self.btn2.setIconSize(QtCore.QSize(240, 65))
        self.btn2.clicked.connect(self.reporting_method)

        self.btn3 = QPushButton("", left)
        self.btn3.setGeometry(15, 107,170, 40)
        self.btn3.setIcon(QtGui.QIcon("Display_Setting.png"))
        self.btn3.setIconSize(QtCore.QSize(240, 65))
        self.btn3.clicked.connect(self.disp_sett)

        self.btn4 = QPushButton("", left)
        self.btn4.setGeometry(15, 150, 170, 40)
        self.btn4.setIcon(QtGui.QIcon("Activate.png"))
        self.btn4.setIconSize(QtCore.QSize(240, 65))

        self.btn5 = QPushButton("", left)
        self.btn5.setGeometry(15, 240, 170, 40)
        self.btn5.setIcon(QtGui.QIcon("Logout.png"))
        self.btn5.setIconSize(QtCore.QSize(240, 65))
        self.btn5.clicked.connect(self.logout_method)

        ######For Settings Tab
        self.label_cam = QLabel("", self.sett)
        self.label_cam.setGeometry(250, 50, 600, 300)
        #self.label_cam.setStyleSheet("background-color:blue")

        self.label_1 = QLabel("Video Configuration Settings",self.sett)
        self.label_1.setGeometry(400,5,300,40)
        self.label_1.setStyleSheet("font-size:20px; font-weight:bold")

        self.label_2 = QLabel("Adjust Brightness", self.sett)
        self.label_2.setGeometry(80, 360, 300, 40)
        self.label_2.setStyleSheet("font-size:16px; font-weight:bold")

        self.slider = QSlider(Qt.Horizontal,self.sett)
        self.slider.setGeometry(90, 410, 380, 40)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setMinimum(10)
        self.slider.setMaximum(300)
        self.slider.setSliderPosition(int(DispSettings.brightness()))
        self.slider.valueChanged.connect(self.slider_change)
        self.label_a = QLabel("0",self.sett)
        self.label_a.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_a.setGeometry(75, 410, 10, 30)
        self.label_b = QLabel(str(DispSettings.brightness()), self.sett)
        self.label_b.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_b.setGeometry(480,410, 30, 30)
        ######FOR CONTRAST
        self.label_3 = QLabel("Adjust Contrast", self.sett)
        self.label_3.setGeometry(595, 360, 300, 40)
        self.label_3.setStyleSheet("font-size:16px; font-weight:bold")

        self.slider2 = QSlider(Qt.Horizontal, self.sett)
        self.slider2.setGeometry(605, 410, 380, 40)
        self.slider2.setFocusPolicy(Qt.StrongFocus)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(100)
        self.slider2.setSliderPosition(int(DispSettings.contrast()))
        self.slider2.valueChanged.connect(self.slider_change1)
        self.label_aa = QLabel("0", self.sett)
        self.label_aa.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_aa.setGeometry(595, 410, 10, 30)
        self.label_ba = QLabel(str(DispSettings.contrast()), self.sett)
        self.label_ba.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_ba.setGeometry(1000, 410, 30, 30)

        ######FOR Saturation
        self.label_4 = QLabel("Adjust Saturation", self.sett)
        self.label_4.setGeometry(80, 460, 300, 40)
        self.label_4.setStyleSheet("font-size:16px; font-weight:bold")

        self.slider3 = QSlider(Qt.Horizontal, self.sett)
        self.slider3.setGeometry(90, 510, 380, 40)
        self.slider3.setFocusPolicy(Qt.StrongFocus)
        self.slider3.setTickPosition(QSlider.TicksBelow)
        self.slider3.setMinimum(10)
        self.slider3.setMaximum(100)
        self.slider3.setSliderPosition(int(DispSettings.saturation()))
        self.slider3.valueChanged.connect(self.slider_change2)
        self.label_ab = QLabel("0", self.sett)
        self.label_ab.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_ab.setGeometry(75, 510, 10, 30)
        self.label_bb = QLabel(str(DispSettings.saturation()), self.sett)
        self.label_bb.setStyleSheet("font-size:14px; font-weight:bold")
        self.label_bb.setGeometry(480, 510, 30, 30)

        self.default_btn = QPushButton("Set Default Settings", self.sett)
        #self.default_btn.setStyleSheet("font-size:12px; font-weight:bold")
        self.default_btn.setGeometry(510, 580, 150, 38)
        self.default_btn.clicked.connect(self.def_sett_apply)


        self.btn_apply = QPushButton("", self.sett)
        self.btn_apply.setGeometry(680, 580, 140, 38)
        self.btn_apply.setIcon(QtGui.QIcon("Apply.png"))
        self.btn_apply.setIconSize(QtCore.QSize(199, 55))
        self.btn_apply.clicked.connect(self.apply_sett)

        self.btn_cancel = QPushButton("", self.sett)
        self.btn_cancel.setGeometry(830, 580, 140, 38)
        self.btn_cancel.setIcon(QtGui.QIcon("Cancel.png"))
        self.btn_cancel.setIconSize(QtCore.QSize(199, 55))
        self.btn_cancel.clicked.connect(self.fun_cancel)
        ####SHOW/HIDE LAYOUTS
        self.reporting_label.hide()
        self.image_label.hide()
        self.center.setVisible(False)
        self.sett.setVisible(False)

        ######WORKING METHODS
        self.kernel_dil = np.ones((20, 20), np.uint8)
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

    def cam_click(self):
        self.a = True
        self.wall.setVisible(False)
        self.sett.setVisible(False)
        self.center.setVisible(True)
        self.image_label.show()
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if ret == True:
                fgmask = self.fgbg.apply(frame)
                fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, self.kernel)
                dilation = cv2.dilate(fgmask, self.kernel_dil, iterations=1)
                (contours, hierarchy) = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for pic, contour in enumerate(contours):
                    area = cv2.contourArea(contour)
                    if (area > 35000):
                        x, y, w, h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        #roi_person = frame[y:y - 10 + h + 5, x:x - 8 + w + 10]

            # Display the resulting frame
            #cv2.imshow('frame', gray)
                self.displayImage(frame,self.image_label, True)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

    def displayImage(self, img, getcamera, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            getcamera.setPixmap(QtGui.QPixmap.fromImage(outImage))
        else:
            self.cap.release()

    def setCamView(self):
        self.a = True
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
        self.cap.set(10, int(DispSettings.brightness()))
        self.cap.set(11, int(DispSettings.contrast()))
        self.cap.set(12, int(DispSettings.saturation()))
        while (True):
            # Capture frame-by-frame
            ret, frame1 = self.cap.read()
            if ret == True:
                self.displayImage(frame1, self.label_cam, True)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def slider_change(self):
        size = self.slider.value()
        self.cap.set(10,size)
        self.label_b.setText(str(size))

    def slider_change1(self):
        size1 = self.slider2.value()
        self.cap.set(11, size1)
        self.label_ba.setText(str(size1))

    def slider_change2(self):
        size2 = self.slider3.value()
        self.cap.set(12,size2)
        self.label_bb.setText(str(size2))

    def reporting_method(self):
        self.ra = ReportAnom.App()
        self.ra.show()

        #self.image_label.hide()
        #self.reporting_label.show()
        #self.reporting_label.setText("aaaaaaaaaaaaa")
        #Wself.fetch()

    def def_sett_apply(self):
        self.slider.setSliderPosition(128)
        self.slider2.setSliderPosition(50)
        self.slider3.setSliderPosition(70)
        DispSettings.confirm(128,50,70)
        Dialog.message("Note","Default Settings Applied!")

    def apply_sett(self):
        x = self.slider.sliderPosition()
        y = self.slider2.sliderPosition()
        z = self.slider3.sliderPosition()
        DispSettings.confirm(x,y,z)
        Dialog.message("Note","Settings Applied Sucessfully!")

    def fun_cancel(self):
        self.cap.release()
        Dialog.message("Note","Settings discarded. Previous saved settings applied")
        self.cam_click()


    def disp_sett(self):
        self.wall.setVisible(False)
        self.center.setVisible(False)
        self.sett.setVisible(True)
        self.setCamView()

    def logout_method(self):
        if self.a == False:
            self.main_lib = main1.Window()
            self.main_lib.show()
            self.hide()
        else:
            self.cap.release()
            sys.exit()
            #self.main_lib2 = main1.Window()
            #self.main_lib2.show()
            #self.close()
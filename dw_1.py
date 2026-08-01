# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:35:58 2026

@author: User
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel
                             ,QWidget,QVBoxLayout,QHBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit 
                             )
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase
class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_lable=QLabel(self)
        self.time=QTimer(self)
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(600,400,300,100)
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)
        self.time_lable.setAlignment(Qt.AlignCenter)
        self.time_lable.setStyleSheet("font-size:150px;"
                                      "color:green;")  
        self.setStyleSheet("background-color:black")
        
        
        font_id=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_Family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_Family,150)
        self.time_lable.setFont(my_font)
        
        self.time.timeout.connect(self.update_time)
        self.time.start(1000)
        
        self.update_time()
        
   
    def update_time(self):
       current_time=QTime.currentTime().toString("hh:mm:ss AP")
       self.time_lable.setText(current_time)
       
           
           



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())


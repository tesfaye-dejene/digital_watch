# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 08:58:06 2026

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

class stop_watch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_lable=QLabel("00:00:00:00",self)
        self.start_button=QPushButton("start",self)
        self.stop_button=QPushButton("stop",self)
        self.reset_button=QPushButton("reset",self)
        self.timer=QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("stop watch")
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_lable)
        
        self.setLayout(vbox)
        self.time_lable.setAlignment(Qt.AlignHCenter)
        
        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           
    QPushButton,QLabel{
        padding:20px;
        font-weight:bold;
        font-family:calibri;
        }                    
    QPushButton {
        font-size: 50px;
    }

    QLabel {
        font-size: 120px;
        background-color: #a7ebe4;
        border-radius:15px;
    }
""")
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_displa)
        
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop() 
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_lable.setText(self.format_time(self.time))
    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        miliseconds=time.msec() // 10
        
        return f"{hours:02}:{minutes:02}:{seconds:02}:{miliseconds:02}"
    def update_displa(self):
        self.time=self.time.addMSecs(10)
        self.time_lable.setText(self.format_time(self.time))
    
       
        
        
        
if __name__ == "__main__":
   app = QApplication(sys.argv)
   stop_watch = stop_watch()
   stop_watch.show()
   sys.exit(app.exec_())
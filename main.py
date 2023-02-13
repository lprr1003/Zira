import sys
from moviepy.editor import *
from tkinter import *

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
# from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from main_ui import Ui_MainWindow
import main_thread


startExecution = main_thread.MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/5initialisingSystem.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/6zira.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/siri2.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)
        # label_query = startExecution.listen()
        # self.ui.textBrowser_3.setText(label_query)


app = QApplication(sys.argv)
Zira = Main()
Zira.show()
exit(app.exec_())


# if __name__ == '__main__':
#     while(True):
#         cmd = listen()
#         if "hey" in cmd:
#             TaskExe()
#         elif "by" or "bye" in cmd:
#             speak("Have a good day")
#             sys.exit()














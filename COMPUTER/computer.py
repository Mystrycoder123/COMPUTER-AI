from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from ComputerUi import Ui_MainWindow
from ComputerUi import Ui_MainWindow 
import sys
import Main

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.TaskExe()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):
        print("hi")

        super().__init__()

        self.Computer_ui = Ui_MainWindow()
        
        self.Computer_ui.setupUi(self)

        self.Computer_ui.pushButton.clicked.connect(self.startFunc)

        self.Computer_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.Computer_ui.movies = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/B.G/1.gif")

        self.Computer_ui.Gif.setMovie(self.Computer_ui.movies)

        self.Computer_ui.movies.start()



        self.Computer_ui.movies_2 = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/VoiceReg/gui (4).gif")

        self.Computer_ui.Gif_2.setMovie(self.Computer_ui.movies_2)

        self.Computer_ui.movies_2.start()




        self.Computer_ui.movies_3 = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/ExtraGui/initial.gif")

        self.Computer_ui.Gif_3.setMovie(self.Computer_ui.movies_3)

        self.Computer_ui.movies_3.start()



        self.Computer_ui.movies_3 = QtGui.QMovie("../../../../2 - Python/3 -  Materials/G.U.I Material/ExtraGui/Earth_Template.gif")

        self.Computer_ui.Gif_3.setMovie(self.Computer_ui.movies_3)

        self.Computer_ui.movies_3.start()



        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):
        
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time 

        self.Computer_ui.textBrowser.setText(labbel)

Gui_App = QApplication(sys.argv)

Gui_Computer = Gui_Start()

Gui_Computer.show()

exit(Gui_App.exec_())

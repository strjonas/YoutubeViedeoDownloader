from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCheckBox
from pytube import YouTube
import re

class Ui_MainWindow(object):

    
    def setupUi(self, MainWindow):
        default = False

        MainWindow.setWindowIcon(QtGui.QIcon('youtube.png'))
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 165)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 20, 491, 31))
        self.textEdit.setObjectName("textEdit")
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 91, 31))
        self.label.setObjectName("label")

        self.defaultbox = QCheckBox(self.centralwidget)
        self.defaultbox.setGeometry(QtCore.QRect(372, 60, 70,31))
        self.defaultbox.setObjectName("defaultbox")
        self.defaultbox.stateChanged.connect(self.defaultres)
        

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(280, 60, 91, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        #350
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 60, 91, 31))
        self.label_5.setObjectName("label_5")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(500, 60, 271 , 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setPlainText('C:/')
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 62, 91, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ytlogo.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 100, 491, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getlink)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 171, 31))
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(174, 100, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.downloadnew)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YoutubeDownloader"))
        self.label.setText(_translate("MainWindow", "EnterLink:"))
        self.label_2.setText(_translate("MainWindow", "EnterResolution"))
        self.pushButton.setText(_translate("MainWindow", "Download Video"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Downlad new"))
        self.label_5.setText(_translate("MainWindow", "Enter Path:"))
        self.defaultbox.setText(_translate("MainWindow", "Default"))

    def getlink(self):
        self.link = self.textEdit.toPlainText()
        self.res = self.textEdit_2.toPlainText()
        self.path = self.textEdit_5.toPlainText()
        if self.link != '':
            self.download(self.link,self.res,self.path)

    def defaultres(self, state):
        if (QtCore.Qt.Checked == state):
            self.textEdit_2.setPlainText('720p')
            self.default = True
        else:
            self.default = False
            self.textEdit_2.setPlainText('')

        
    def downloadnew(self):
      
        _translate = QtCore.QCoreApplication.translate
    
        self.textEdit.setPlainText('')
     
        self.textEdit_2.setPlainText('')
      
        self.textEdit_5.setPlainText('')
     
        self.link = ''
    
        self.res = ''
        self.path = ''
        self.label_4.setText(_translate("MainWindow", ""))

        
    def download(self,link,res,path):
        try:
            _translate = QtCore.QCoreApplication.translate
            self.label_4.setText(_translate("MainWindow", "Loading..."))
        
            yt = YouTube(link)
        
            if self.default:
                res = '720p'
        
            c =yt.streams.filter(resolution=res, file_extension='mp4')
        
            f = str(c).split()
            m =f[1]
            r = re.findall(r'\d',m)
            m ="".join(r)
            yt.streams.get_by_itag(int(m)).download(output_path=path)
            self.label_4.setText(_translate("MainWindow", "succesfully downloaded"))
        except:
            self.label_4.setText(_translate("MainWindow", "Invalid path, link or resolution"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.getlink()
    sys.exit(app.exec_())

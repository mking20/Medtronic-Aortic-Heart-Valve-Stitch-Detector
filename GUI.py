# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(20, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnBrowse.setFont(font)
        self.btnBrowse.setAutoDefault(False)
        self.btnBrowse.setDefault(False)
        self.btnBrowse.setFlat(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(770, 580, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnalyze.setGeometry(QtCore.QRect(130, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnAnalyze.setFont(font)
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(510, 120, 481, 451))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(10)
        self.lblResult.setFont(font)
        self.lblResult.setTextFormat(QtCore.Qt.AutoText)
        self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResult.setObjectName("lblResult")
        self.txtNRI = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNRI.setGeometry(QtCore.QRect(620, 580, 131, 31))
        self.txtNRI.setObjectName("txtNRI")
        self.lblImage = QtWidgets.QLabel(self.centralwidget)
        self.lblImage.setGeometry(QtCore.QRect(20, 120, 481, 451))
        self.lblImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lblImage.setText("")
        self.lblImage.setObjectName("lblImage")
        self.lblMLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblMLogo.setGeometry(QtCore.QRect(20, 580, 151, 41))
        self.lblMLogo.setText("")
        self.lblMLogo.setPixmap(QtGui.QPixmap("med.png"))
        self.lblMLogo.setScaledContents(True)
        self.lblMLogo.setObjectName("lblMLogo")
        self.lblCLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblCLogo.setGeometry(QtCore.QRect(870, 10, 111, 91))
        self.lblCLogo.setText("")
        self.lblCLogo.setPixmap(QtGui.QPixmap("cetys.png"))
        self.lblCLogo.setScaledContents(True)
        self.lblCLogo.setObjectName("lblCLogo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnBrowse.clicked.connect(self.setImage)
        self.btnAnalyze.clicked.connect(self.getAnalyzed)
        self.btnSave.clicked.connect(self.getSaved) 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medtronic Aortic Heart Valve Stitch Detector"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnAnalyze.setText(_translate("MainWindow", "Analyze"))
        self.lblResult.setText(_translate("MainWindow", "Tentative Result"))
    def setImage(self):
        fileName, _=QtWidgets.QFileDialog.getOpenFileName(None, "Browse","","Image Files (*.png *.jpg *.jpeg *.bmp) ;;All Files(*)")#Ask for Image File
        if fileName: #If the user gives a file
            pixmap = QtGui.QPixmap(fileName) #Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.lblImage.width(), self.lblImage.height(), QtCore.Qt.KeepAspectRatio)#Scale pixmap
            self.lblImage.setPixmap(pixmap)#Set the pixmap into the label
            self.lblImage.setAlignment(QtCore.Qt.AlignCenter)#Align the label to center
            
    def getAnalyzed(self):
        print("Analyzing...")
        image = self.lblImage.pixmap()
        self.lblResult.setPixmap(image)
        
    def getSaved(self):
        fileName, _=QtWidgets.QFileDialog.getSaveFileName(None, "Browse",self.txtNRI.toPlainText(),"Image Files (*.png *.jpg *.jpeg *.bmp) ;;All Files(*)")
        imageResult = self.lblResult.pixmap()
        with open('mytextfile.txt', 'w') as f:
            f.write(fileName)
        imageResult.save(fileName,quality = 100)

        self.lblResult.clear()
        self.lblImage.clear()
        self.txtNRI.clear()
        
        print(fileName)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


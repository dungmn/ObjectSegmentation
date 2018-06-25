# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Segmen import Segmentation
from functools import partial
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.path=''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 1041, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgRaw = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.imgRaw.setFont(font)
        self.imgRaw.setAutoFillBackground(False)
        self.imgRaw.setFrameShape(QtWidgets.QFrame.Box)
        self.imgRaw.setScaledContents(False)
        self.imgRaw.setAlignment(QtCore.Qt.AlignCenter)
        self.imgRaw.setWordWrap(False)
        self.imgRaw.setIndent(1)
        self.imgRaw.setObjectName("imgRaw")
        self.horizontalLayout.addWidget(self.imgRaw)
        self.imgResult = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.imgResult.setFont(font)
        self.imgResult.setAutoFillBackground(False)
        self.imgResult.setFrameShape(QtWidgets.QFrame.Box)
        self.imgResult.setScaledContents(False)
        self.imgResult.setAlignment(QtCore.Qt.AlignCenter)
        self.imgResult.setWordWrap(False)
        self.imgResult.setIndent(1)
        self.imgResult.setObjectName("imgResult")
        self.horizontalLayout.addWidget(self.imgResult)
        self.btnExcute = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcute.setGeometry(QtCore.QRect(430, 400, 89, 25))
        self.btnExcute.setObjectName("btnExcute")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 430, 1041, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)
        self.txtResult = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.txtResult.setEnabled(True)
        font = QtGui.QFont()
        font.setItalic(True)
        self.txtResult.setFont(font)
        self.txtResult.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.txtResult.setReadOnly(True)
        self.txtResult.setCenterOnScroll(False)
        self.txtResult.setObjectName("txtResult")
        self.horizontalLayout_2.addWidget(self.txtResult)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 681, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.txtThress = QtWidgets.QLineEdit(self.centralwidget)
        self.txtThress.setGeometry(QtCore.QRect(310, 400, 113, 25))
        self.txtThress.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtThress.setObjectName("txtThress")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.allEvents()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imgRaw.setText(_translate("MainWindow", "<html><head/><body><p>Click Here To Load Image</p></body></html>"))
        self.imgResult.setText(_translate("MainWindow", "Image Result"))
        self.btnExcute.setText(_translate("MainWindow", "Excute"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "OBJECT SEGMENTATION USING MEANSHIFT ALGORITHM\n"
"\n"
"Lecturers: Le Dinh Duy - Nguyen Vinh Tiep\n"
"\n"
"Student 1: Nguyen Quoc Danh - 15520092\n"
"Student 2: Nguyen Minh Dung - 15520138"))
        self.txtResult.setPlainText(_translate("MainWindow", "\n"
"\n"
"\n"
"--------------------------------------------------READY------------------------------------------------------"))
        self.txtThress.setPlaceholderText(_translate("MainWindow", "Radius"))
    def allEvents(self):
        # self.imgResult.mousePressEvent = partial(self.fileSelector,self.imgResult)
        self.imgRaw.mousePressEvent = partial(self.fileSelector,self.imgRaw)
        self.btnExcute.clicked.connect(self.excute)
    def fileSelector(self,label,event):
        filenames,_ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Data", "", "*")
        pixmap = QtGui.QPixmap(filenames)
        w =label.width()
        h = label.height()
        label.setPixmap(pixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio))
        self.path = filenames
    def excute(self):
        result = "--------------------------------------------------LOADING-------------------------------------------------"
        self.txtResult.setPlainText(result)
        radius = self.txtThress.text()
        if self.path=='':
            self.txtResult.setPlainText("ERROR PATH IMAGE. PLEASE CHOOSE IMAGE")
            return
        try:
            number = int(radius)
            obj = Segmentation(self.path,radius=radius)
            pathImgResult,result = obj.excute()
            strResult = "Number of Clusters: "+ str(result[0]) + '\nTime: '+str(result[1])+"s"+'\nSize of Image (WidthxHeight): '+str(result[2])+"\nPath Image_Result: "+str(result[3])
            self.txtResult.setPlainText(strResult)
            qPixmap = QtGui.QPixmap(pathImgResult)
            w =self.imgResult.width()
            h = self.imgResult.height()
            self.imgResult.setPixmap(qPixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio))
        except :
            QtWidgets.QMessageBox.about(None, 'Error','Input can only be a number')
            self.txtResult.setPlainText("--------------------------------------------------READY----------------------------------------------------")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

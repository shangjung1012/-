# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shangjung/Desktop/自主學習/qt_designer/biopython.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folder_path = QtWidgets.QTextEdit(self.centralwidget)
        self.folder_path.setGeometry(QtCore.QRect(170, 200, 281, 31))
        self.folder_path.setObjectName("folder_path")
        self.change_folder = QtWidgets.QPushButton(self.centralwidget)
        self.change_folder.setGeometry(QtCore.QRect(470, 200, 121, 26))
        self.change_folder.setObjectName("change_folder")
        self.Download_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Download_Button.setGeometry(QtCore.QRect(360, 260, 91, 26))
        self.Download_Button.setObjectName("Download_Button")
        self.reminder = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.reminder.setGeometry(QtCore.QRect(200, 50, 321, 51))
        self.reminder.setObjectName("reminder")
        self.genus = QtWidgets.QLineEdit(self.centralwidget)
        self.genus.setGeometry(QtCore.QRect(210, 130, 211, 31))
        self.genus.setText("")
        self.genus.setClearButtonEnabled(True)
        self.genus.setObjectName("genus")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 300, 301, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.logview = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.logview.setObjectName("logview")
        self.gridLayout.addWidget(self.logview, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.change_folder.setText(_translate("MainWindow", "change folder"))
        self.Download_Button.setText(_translate("MainWindow", "Download"))
        self.reminder.setPlainText(_translate("MainWindow", "輸入要下載的，如有多個，中間以分號隔開，例如\n"
"Culter;Chanodichthys;Megalobrama"))
        self.genus.setPlaceholderText(_translate("MainWindow", "genus1;genus2;genus3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

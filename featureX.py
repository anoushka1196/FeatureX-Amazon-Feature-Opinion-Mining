from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_RunWindow

class Ui_FeatureXWindow(object):
    def setupUi(self, FeatureXWindow):
        FeatureXWindow.setObjectName("FeatureXWindow")
        FeatureXWindow.resize(1366, 768)
        FeatureXWindow.setWindowIcon(QtGui.QIcon('images/fx.png'))
        FeatureXWindow.setStyleSheet("#FeatureXWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(FeatureXWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 100, 850, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(60)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(610, 380, 220, 170))
        self.goButton.setObjectName("goButton")
        self.goButton.setStyleSheet("#goButton{background-color:transparent; }")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(48)
        font.setBold(True)
        self.goButton.setFont(font)
        FeatureXWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FeatureXWindow)
        self.statusbar.setObjectName("statusbar")
        FeatureXWindow.setStatusBar(self.statusbar)
        self.retranslateUi(FeatureXWindow)
        QtCore.QMetaObject.connectSlotsByName(FeatureXWindow)

    def retranslateUi(self, FeatureXWindow):
        _translate = QtCore.QCoreApplication.translate
        FeatureXWindow.setWindowTitle(_translate("FeatureXWindow", "FeatureX"))
        self.label.setText(_translate("FeatureXWindow", "Welcome to FeatureX"))
        self.goButton.setText(_translate("FeatureXWindow", "GO ->"))
        #ourStuff
        self.goButton.clicked.connect(self.openMaingui)

    #our function
    def openMaingui(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_RunWindow()
        self.ui.setupUi(self.window)
        FeatureXWindow.hide()  # close current window
        self.window.show()  # open new window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FeatureXWindow = QtWidgets.QMainWindow()
    ui = Ui_FeatureXWindow()
    ui.setupUi(FeatureXWindow)
    FeatureXWindow.show()
    sys.exit(app.exec_())

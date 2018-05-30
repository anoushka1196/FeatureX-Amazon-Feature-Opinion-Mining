from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Ui_Dashboard
import Asin
import Run

class Ui_RunWindow(object):
    def setupUi(self, RunWindow):
        RunWindow.setObjectName("RunWindow")
        RunWindow.resize(1366, 768)
        RunWindow.setWindowIcon(QtGui.QIcon('images/crawl.png'))
        RunWindow.setStyleSheet("#RunWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        RunWindow.setFont(font)
        RunWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(RunWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProductCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ProductCombo.setGeometry(QtCore.QRect(935, 230, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.ProductCombo.setFont(font)
        self.ProductCombo.setEditable(False)
        self.ProductCombo.setCurrentText("")
        self.ProductCombo.setObjectName("ProductCombo")
        self.ProductCombo.setStyleSheet("#ProductCombo{background:transparent;border:1px solid;}");
        self.SummaryButton = QtWidgets.QPushButton(self.centralwidget)
        self.SummaryButton.setGeometry(QtCore.QRect(855, 450, 220, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.SummaryButton.setFont(font)
        self.SummaryButton.setObjectName("SummaryButton")
        # self.SummaryButton.setStyleSheet("background-color: transparent")
        # self.SummaryButton.setStyleSheet("#SummaryButton{background:solid;border:1px solid;}");
        self.Asintext = QtWidgets.QLineEdit(self.centralwidget)
        self.Asintext.setEnabled(True)
        self.Asintext.setGeometry(QtCore.QRect(935, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Asintext.setFont(font)
        self.Asintext.setObjectName("Asintext")
        self.RadioGroup1 = QtWidgets.QGroupBox(self.centralwidget)
        self.RadioGroup1.setGeometry(QtCore.QRect(650, 110, 251, 291))
        self.RadioGroup1.setAutoFillBackground(False)
        self.RadioGroup1.setTitle("")
        self.RadioGroup1.setObjectName("RadioGroup1")
        self.AsinRadio = QtWidgets.QRadioButton(self.RadioGroup1)
        self.AsinRadio.setGeometry(QtCore.QRect(20, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.AsinRadio.setFont(font)
        self.AsinRadio.setObjectName("AsinRadio")
        self.BrandRadio = QtWidgets.QRadioButton(self.RadioGroup1)
        self.BrandRadio.setGeometry(QtCore.QRect(20, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.BrandRadio.setFont(font)
        self.BrandRadio.setObjectName("BrandRadio")
        self.ProductLabel = QtWidgets.QLabel(self.RadioGroup1)
        self.ProductLabel.setGeometry(QtCore.QRect(40, 125, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.ProductLabel.setFont(font)
        self.ProductLabel.setObjectName("ProductLabel")
        self.BrandCombo = QtWidgets.QComboBox(self.centralwidget)
        self.BrandCombo.setGeometry(QtCore.QRect(935, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.BrandCombo.setFont(font)
        self.BrandCombo.setEditable(False)
        self.BrandCombo.setCurrentText("")
        self.BrandCombo.setObjectName("BrandCombo")
        self.BrandCombo.setStyleSheet("#BrandCombo{background:transparent;border:1px solid;}");
        self.PicLabel = QtWidgets.QLabel(self.centralwidget)
        self.PicLabel.setGeometry(QtCore.QRect(150, 110, 261, 290))
        self.PicLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.PicLabel.setText("")
        self.PicLabel.setObjectName("PicLabel")
        self.PicLabel.setStyleSheet("#PicLabel { border-image: url(images/fx.png) 0 0 0 0 stretch stretch; }")
        RunWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RunWindow)
        self.statusbar.setObjectName("statusbar")
        RunWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RunWindow)
        QtCore.QMetaObject.connectSlotsByName(RunWindow)

    def retranslateUi(self, RunWindow):
        _translate = QtCore.QCoreApplication.translate
        RunWindow.setWindowTitle(_translate("RunWindow", "Review Summarizer"))
        self.SummaryButton.setText(_translate("RunWindow", "Generate Summary"))
        self.AsinRadio.setText(_translate("RunWindow", "Enter ASIN"))
        self.BrandRadio.setText(_translate("RunWindow", "Select Brand"))
        self.ProductLabel.setText(_translate("RunWindow", "Select product"))

        #our stuff
        self.BrandRadio.setChecked(True)
        self.BrandCombo.addItem("Moto")
        self.BrandCombo.addItem("Samsung")
        self.BrandCombo.currentIndexChanged.connect(self.addProduct)

        self.addProduct()
        self.radio()
        self.BrandRadio.toggled.connect(self.radio)
        self.AsinRadio.toggled.connect(self.radio)
        self.SummaryButton.clicked.connect(self.onClick)

    def addProduct(self):
        brand = str(self.BrandCombo.currentText())
        if(brand == "Moto"):
            self.ProductCombo.clear()
            self.ProductCombo.addItem("Moto G5") #B071WDBTW1
            self.ProductCombo.addItem("Moto G Play")  #B079SGQNPN
            self.ProductCombo.addItem("Moto Z") #B079YM4RXS
            self.ProductCombo.addItem("Moto Z Play")  #B01LW9P0H4
        elif(brand == "Samsung"):
            self.ProductCombo.clear()
            self.ProductCombo.addItem("Samsung Galaxy S8") #B06Y137TLR
            self.ProductCombo.addItem("Samsung Galaxy S8+") #B06Y15G61T
            self.ProductCombo.addItem("Samsung Galaxy S9") #B079JSZ1Z2
            self.ProductCombo.addItem("Samsung S7 Edge")   #B01M7O431L

    def radio(self):
        if (self.BrandRadio.isChecked() == True):
            self.BrandCombo.setEnabled(True)
            self.ProductCombo.setEnabled(True)
            self.Asintext.clear()
            self.Asintext.setEnabled(False)
        if (self.AsinRadio.isChecked() == True):
            self.BrandCombo.setEnabled(False)
            self.ProductCombo.setEnabled(False)
            self.Asintext.setEnabled(True)

    def onClick(self):
        if (self.BrandRadio.isChecked() == True):
            product = str(self.ProductCombo.currentText())
            textboxValue=Asin.getAsinCompare(product)
            Run.crawl(textboxValue)
            Run.convert(textboxValue)
            self.setAsin(textboxValue)
            self.openDashboard()
        elif (self.AsinRadio.isChecked() == True):
            textboxValue = self.Asintext.text()
            if(len(textboxValue)!=10):
                msgbox = QtWidgets.QMessageBox()
                msgbox.setGeometry(550, 340, 600, 450)
                msgbox.setIcon(QtWidgets.QMessageBox.Warning)
                msgbox.setText("Please enter valid ASIN!")
                msgbox.setWindowTitle("Error")
                msgbox.setEscapeButton(QtWidgets.QMessageBox.Close)
                msgbox.exec_()
                self.Asintext.clear()
            else:
                Run.crawl(textboxValue)
                Run.convert(textboxValue)
                self.setAsin(textboxValue)
                self.openDashboard()
        # Run.crawl(textboxValue)
        # Run.convert(textboxValue)
        # self.setAsin(textboxValue)
        # self.openDashboard()

    def openDashboard(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.window)
        self.window.show()  # open new window
        #RunWindow.hide()   # hide current window

    def setAsin(self,AsinValue):
        Asin.setAsinValue(AsinValue)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RunWindow = QtWidgets.QMainWindow()
    ui = Ui_RunWindow()
    ui.setupUi(RunWindow)
    RunWindow.show()
    sys.exit(app.exec_())


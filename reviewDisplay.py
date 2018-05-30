from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import Asin
import Run

class Ui_ReviewsWindow(object):
    def setupUi(self, ReviewsWindow):
        ReviewsWindow.setObjectName("ReviewsWindow")
        ReviewsWindow.resize(1366, 768)
        ReviewsWindow.setWindowIcon(QtGui.QIcon('images/review.png'))
        ReviewsWindow.setStyleSheet("#ReviewsWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(ReviewsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.featurecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.featurecomboBox.setGeometry(QtCore.QRect(650, 30, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.featurecomboBox.setFont(font)
        self.featurecomboBox.setObjectName("featurecomboBox")
        self.featurecomboBox.setStyleSheet("#featurecomboBox{background:transparent;border:1px solid;}");
        self.featureSelectLabel = QtWidgets.QLabel(self.centralwidget)
        self.featureSelectLabel.setGeometry(QtCore.QRect(390, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.featureSelectLabel.setFont(font)
        self.featureSelectLabel.setObjectName("featureSelectLabel")
        self.positiveList = QtWidgets.QListWidget(self.centralwidget)
        self.positiveList.setGeometry(QtCore.QRect(20, 160, 641, 455))
        self.positiveList.setWordWrap(True)
        self.positiveList.setSpacing(3)
        self.positiveList.setObjectName("positiveList")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.positiveList.setFont(font)
        self.negativeList = QtWidgets.QListWidget(self.centralwidget)
        self.negativeList.setGeometry(QtCore.QRect(690, 160, 641, 455))
        self.negativeList.setWordWrap(True)
        self.negativeList.setSpacing(3)
        self.negativeList.setObjectName("negativeList")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.negativeList.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 110, 171, 41))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(940, 110, 171, 41))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        ReviewsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReviewsWindow)
        self.statusbar.setObjectName("statusbar")
        ReviewsWindow.setStatusBar(self.statusbar)
        self.retranslateUi(ReviewsWindow)
        QtCore.QMetaObject.connectSlotsByName(ReviewsWindow)

    def retranslateUi(self, ReviewsWindow):
        _translate = QtCore.QCoreApplication.translate
        ReviewsWindow.setWindowTitle(_translate("ReviewsWindow", "Reviews"))
        self.featureSelectLabel.setText(_translate("ReviewsWindow", "Select Feature"))
        self.label.setText(_translate("ReviewsWindow", "Positive Reviews"))
        self.label_2.setText(_translate("ReviewsWindow", "Negative Reviews"))

        #our stuff
        self.featurecomboBox.addItem("All")
        self.featurecomboBox.addItem("Camera")
        self.featurecomboBox.addItem("Battery")
        self.featurecomboBox.addItem("Screen")
        self.featurecomboBox.addItem("Memory")
        self.featurecomboBox.addItem("Size")
        self.featurecomboBox.addItem("Audio")
        self.featurecomboBox.addItem("Processor")
        asin = Asin.getAsinValue()
        Run.pos_neg(asin)
        self.show(asin)
        self.featurecomboBox.currentIndexChanged.connect(self.search)

    def show(self,asinValue):
        posFile = open("Datasets/"+asinValue+"_folder/"+asinValue + "_pos.txt","r")
        negFile = open("Datasets/"+asinValue+"_folder/"+asinValue + "_neg.txt", "r")
        csv_p = csv.reader(posFile, delimiter = "\n")
        csv_n = csv.reader(negFile, delimiter = "\n")
        a=1
        for row in csv_p:
            for i in row:
                text = str(a) + ") " + i
                self.positiveList.addItem(text)
                a+=1
        b=1
        for row in csv_n:
            for i in row:
                text = str(b) + ") " + i
                self.negativeList.addItem(text)
                b+=1

    def search(self):
       asinValue = Asin.getAsinValue()
       feature = str(self.featurecomboBox.currentText())
       self.positiveList.clear()
       self.negativeList.clear()
       if (feature == 'All'):
           self.show(asinValue)
       elif (feature == 'Camera'):
           search_for = ['camera','picture','photo']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Battery'):
           search_for = ['battery','drain','discharge']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Screen'):
           search_for = ['screen','display','touch','glass']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Processor'):
           search_for = ['processor','speed','processing speed']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Memory'):
           search_for = ['memory',' ram ',' rom ','storage','sd card']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Size'):
           search_for = ['size','dimensiion','weight']
           self.implicitsearch(asinValue,search_for)
       elif (feature == 'Audio'):
           search_for = ['audio','sound','music','noise']
           self.implicitsearch(asinValue,search_for)

    def implicitsearch(self,asinValue,search_for):
        posFile = open("Datasets/"+asinValue+"_folder/"+asinValue + "_pos.txt", "r")
        negFile = open("Datasets/"+asinValue+"_folder/"+asinValue + "_neg.txt", "r")
        csv_p = csv.reader(posFile, delimiter="\n")
        csv_n = csv.reader(negFile, delimiter="\n")
        a = 1
        for row in csv_p:
           for i in row:
                for j in search_for:
                    if (j in i):
                        text = str(a) + ") " + i
                        self.positiveList.addItem(text)
                        a += 1
                        break
        b=1
        for row in csv_n:
           for i in row:
                for j in search_for:
                    if(j in i):
                        text = str(b) + ") " + i
                        self.negativeList.addItem(text)
                        b += 1
                        break



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewsWindow = QtWidgets.QMainWindow()
    ui = Ui_ReviewsWindow()
    ui.setupUi(ReviewsWindow)
    ReviewsWindow.show()
    sys.exit(app.exec_())
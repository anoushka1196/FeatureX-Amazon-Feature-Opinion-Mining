from PyQt5 import QtCore, QtGui, QtWidgets
import Asin
import algo
import csv

class Ui_CompareWindow(object):
    def setupUi(self, CompareWindow):
        CompareWindow.setObjectName("CompareWindow")
        CompareWindow.resize(1366, 768)
        CompareWindow.setWindowIcon(QtGui.QIcon('images/compare.png'))
        CompareWindow.setStyleSheet("#CompareWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(CompareWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.product1Text = QtWidgets.QListWidget(self.centralwidget)
        self.product1Text.setGeometry(QtCore.QRect(270, 140, 391, 521))
        self.product1Text.setObjectName("product1Text")
        self.product1Text.setSpacing(4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.product1Text.setFont(font)
        self.product2Text = QtWidgets.QListWidget(self.centralwidget)
        self.product2Text.setGeometry(QtCore.QRect(740, 140, 391, 521))
        self.product2Text.setObjectName("product2Text")
        self.product2Text.setSpacing(4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.product2Text.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 60, 125, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(900, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("#comboBox{background:transparent;border:1px solid;}");
        self.product1Label = QtWidgets.QLabel(self.centralwidget)
        self.product1Label.setGeometry(QtCore.QRect(300, 60, 260, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.product1Label.setFont(font)
        #self.product1Label.setFrameShape(QtWidgets.QFrame.Box)
        # self.product1Label.setLineWidth(1)
        self.product1Label.setObjectName("product1Label")
        #self.product1Label.setAlignment(QtCore.Qt.AlignCenter)
        CompareWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CompareWindow)
        self.statusbar.setObjectName("statusbar")
        CompareWindow.setStatusBar(self.statusbar)
        self.retranslateUi(CompareWindow)
        QtCore.QMetaObject.connectSlotsByName(CompareWindow)

    def retranslateUi(self, CompareWindow):
        _translate = QtCore.QCoreApplication.translate
        CompareWindow.setWindowTitle(_translate("CompareWindow", "Compare Products"))
        self.label.setText(_translate("CompareWindow", "Select Product"))

        #our stuff
        asin = Asin.getAsinValue()
        name=Asin.getPhoneName(asin)
        self.product1Label.setText(name)

        if (name != 'Moto G5'):
           self.comboBox.addItem("Moto G5")
        if (name != 'Moto G Play'):
           self.comboBox.addItem("Moto G Play")
        if (name != 'Moto Z'):
           self.comboBox.addItem("Moto Z")
        if (name!='Moto Z Play'):
           self.comboBox.addItem("Moto Z Play")
        if (name != 'Samsung Galaxy S8'):
           self.comboBox.addItem("Samsung Galaxy S8")
        if (name != 'Samsung Galaxy S8+'):
           self.comboBox.addItem("Samsung Galaxy S8+")
        if (name != 'Samsung Galaxy S9'):
           self.comboBox.addItem("Samsung Galaxy S9")
        if (name != 'Samsung S7 Edge'):
           self.comboBox.addItem("Samsung S7 Edge")

        self.showscores(asin)
        self.compareProduct()
        self.comboBox.currentIndexChanged.connect(self.compareProduct)

    def showscores(self,asin):
        key_rating_d = algo.noun_dict()
        cost = Asin.getPrice(asin)
        self.product1Text.addItem("MRP\t\t : \t" + cost)
        for keys, values in key_rating_d.items():
            for i in values:
                s = i.split('/')
            value = keys + "\t\t : \t" + str(s[0]).rstrip(" ")
            self.product1Text.addItem(value)

    def compareProduct(self):
        asinVal1 = Asin.getAsinValue()
        ipFile1 = open("Datasets/" + asinVal1 + "_folder/" + asinVal1 + "_compare.csv", "r")
        name = str(self.comboBox.currentText())
        asinVal2=Asin.getAsinCompare(name)
        ipFile2 = open("Datasets/"+asinVal2+"_folder/" + asinVal2 + "_compare.csv", "r")

        #########---------------File 1
        csv_f1 = csv.reader(ipFile1)
        self.product1Text.clear()
        cost = Asin.getPrice(asinVal1)
        self.product1Text.addItem("MRP\t\t : \t" + cost)

        #########---------------File 2
        self.product2Text.clear()
        cost = Asin.getPrice(asinVal2)
        self.product2Text.addItem("MRP\t\t : \t" + cost)
        list = []

        for row1 in csv_f1:
            feature = row1[0]
            #print("f : " + feature)

            ipFile2.seek(0)
            csv_f2 = csv.reader(ipFile2)
            for row2 in csv_f2:
                if(row2[0] == feature):
                    s1 = row1[1].split('/')
                    value1 = row1[0] + "\t\t : \t" + str(s1[0]).strip("['")
                    self.product1Text.addItem(str(value1).rstrip(" "))
                    s2 = row2[1].split('/')
                    value2 = row2[0] + "\t\t : \t" + str(s2[0]).strip("['")
                    self.product2Text.addItem(str(value2).rstrip(" "))

                    list.append(feature)
                    break
                else:
                    continue

        # print(list)

        ipFile1.seek(0)
        csv_f1 = csv.reader(ipFile1)
        for row in csv_f1:
            if(row[0] in list):
                continue
            else:
                s = row[1].split('/')
                value = row[0] + "\t\t : \t" + str(s[0]).strip("['")
                self.product1Text.addItem(str(value).rstrip(" "))
        ipFile1.close()

        ipFile2.seek(0)
        csv_f2 = csv.reader(ipFile2)
        for row in csv_f2:
            if (row[0] in list):
                continue
            else:
                s = row[1].split('/')
                value = row[0] + "\t\t : \t" + str(s[0]).strip("['")
                self.product2Text.addItem(str(value).rstrip(" "))
        ipFile2.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CompareWindow = QtWidgets.QMainWindow()
    ui = Ui_CompareWindow()
    ui.setupUi(CompareWindow)
    CompareWindow.show()
    sys.exit(app.exec_())


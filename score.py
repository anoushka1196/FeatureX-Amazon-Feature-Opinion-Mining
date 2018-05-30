# from PyQt5.QtWidgets import QVBoxLayout
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#plt.rcdefaults()
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import algo
import Asin

class Ui_ScoreWindow(object):
    def setupUi(self, ScoreWindow):
        ScoreWindow.setObjectName("ScoreWindow")
        ScoreWindow.resize(1366, 768)
        ScoreWindow.setWindowIcon(QtGui.QIcon('images/score.png'))
        ScoreWindow.setStyleSheet("#ScoreWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(ScoreWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.featureView = QtWidgets.QGraphicsView(self.centralwidget)
        self.featureView.setGeometry(QtCore.QRect(20, 90, 625, 440))
        self.featureView.setObjectName("featureView")
        self.serviceView = QtWidgets.QGraphicsView(self.centralwidget)
        self.serviceView.setGeometry(QtCore.QRect(670, 90, 645, 440))
        self.serviceView.setObjectName("serviceView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 580, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.featureCombo = QtWidgets.QComboBox(self.centralwidget)
        self.featureCombo.setGeometry(QtCore.QRect(530, 580, 231, 41))
        self.featureCombo.setObjectName("featureCombo")
        self.featureCombo.setStyleSheet("#featureCombo{background:transparent;border:1px solid;}");
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.featureCombo.setFont(font)
        self.scoreText = QtWidgets.QLineEdit(self.centralwidget)
        self.scoreText.setGeometry(QtCore.QRect(840, 580, 141, 41))
        self.scoreText.setObjectName("scoreText")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.scoreText.setFont(font)

        ScoreWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ScoreWindow)
        self.statusbar.setObjectName("statusbar")
        ScoreWindow.setStatusBar(self.statusbar)
        self.retranslateUi(ScoreWindow)
        QtCore.QMetaObject.connectSlotsByName(ScoreWindow)

    def retranslateUi(self, ScoreWindow):
        _translate = QtCore.QCoreApplication.translate
        ScoreWindow.setWindowTitle(_translate("ScoreWindow", "Feature Based Scores"))
        self.label.setText(_translate("ScoreWindow", "Feature-Score"))
        self.label_2.setText(_translate("ScoreWindow", "Service-Score"))
        self.label_3.setText(_translate("ScoreWindow", "Select specific feature"))

        #our stuff
        asin=Asin.getAsinValue()
        self.showscores(asin)
        self.showServiceScore(asin)
        self.featureCombo.currentIndexChanged.connect(self.showValue)

    #our function
    def showscores(self,asin):
        key_rating_d = algo.noun_dict()
        objects = key_rating_d.keys()
        performance = []
        y_pos = np.arange(len(objects))
        for l in key_rating_d.values():
            for i in l:
                # print(i)
                s = i.split('/')
                performance.append(float(s[0]))
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Rating out of 10')
        plt.title('Feature-Score')
        plt.plot(performance, objects)
        plt.savefig('images/'+asin+'_feature.png')
        self.featureView.setStyleSheet("#featureView{border-image:url(images/"+asin+"_feature.png)}")
        # self.canvas.draw()

        self.featureCombo.addItem("Select feature")
        for obs in objects:
            self.featureCombo.addItem(str(obs))

        plt.cla
        plt.close()


    def showServiceScore(self,asin):
        key_rating_d = algo.service_dict()
        objects1 = key_rating_d.keys()
        performance = []
        y_pos = np.arange(len(objects1))
        for l in key_rating_d.values():
            for i in l:
                # print(i)
                s = i.split('/')
                performance.append(float(s[0]))
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects1)
        plt.xlabel('Rating out of 10')
        plt.title('Service-Score')
        plt.plot(performance, objects1)
        plt.savefig('images/'+asin+'_service.png')
        self.serviceView.setStyleSheet("#serviceView{border-image:url(images/"+asin+"_service.png)}")
        # self.canvas1.draw()
        plt.close()

    def showValue(self):
        key_d = algo.noun_dict()
        feature = self.featureCombo.currentText()
        if feature in key_d.keys():
            l = []
            for li in key_d[feature]:
                l.append(li)
            self.scoreText.setText(l[0])
        else:
            self.scoreText.setText('-')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScoreWindow = QtWidgets.QMainWindow()
    ui = Ui_ScoreWindow()
    ui.setupUi(ScoreWindow)
    ScoreWindow.show()
    sys.exit(app.exec_())


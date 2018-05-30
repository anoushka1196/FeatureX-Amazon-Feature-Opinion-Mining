from PyQt5 import QtCore, QtGui, QtWidgets
from reviewDisplay import Ui_ReviewsWindow
from score import Ui_ScoreWindow
from compare import Ui_CompareWindow
from analyse import Ui_AnalysisWindow
import Asin
import algo
import image

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(1366, 768)
        Dashboard.setWindowIcon(QtGui.QIcon('images/dashboard.png'))
        Dashboard.setStyleSheet("#Dashboard { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.showReviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.showReviewButton.setGeometry(QtCore.QRect(150, 60, 221, 111))
        self.showReviewButton.setStyleSheet("#showReviewButton{background:transparent;border:1px solid;}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.showReviewButton.setFont(font)
        self.showReviewButton.setObjectName("showReviewButton")
        self.showScoreButton = QtWidgets.QPushButton(self.centralwidget)
        #self.showScoreButton.setGeometry(QtCore.QRect(720, 170, 221, 151))
        self.showScoreButton.setGeometry(QtCore.QRect(420, 60, 221, 111))
        self.showScoreButton.setStyleSheet("#showScoreButton{background:transparent;border:1px solid;}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.showScoreButton.setFont(font)
        self.showScoreButton.setObjectName("showScoreButton")
        self.compareButton = QtWidgets.QPushButton(self.centralwidget)
        #self.compareButton.setGeometry(QtCore.QRect(440, 370, 221, 151))
        self.compareButton.setGeometry(QtCore.QRect(690, 60, 221, 111))
        self.compareButton.setStyleSheet("#compareButton{background:transparent;border:1px solid;}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.compareButton.setFont(font)
        self.compareButton.setObjectName("compareButton")
        self.analysisButton = QtWidgets.QPushButton(self.centralwidget)
        #self.analysisButton.setGeometry(QtCore.QRect(720, 370, 221, 151))
        self.analysisButton.setGeometry(QtCore.QRect(960, 60, 221, 111))
        self.analysisButton.setStyleSheet("#analysisButton{background:transparent;border:1px solid;}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.analysisButton.setFont(font)
        self.analysisButton.setObjectName("analysisButton")
        self.picLabel = QtWidgets.QLabel(self.centralwidget)
        self.picLabel.setGeometry(QtCore.QRect(330, 300, 300, 321))
        self.picLabel.setObjectName("picLabel")
        self.infoLabel = QtWidgets.QTextEdit(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(730, 300, 555, 300))
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setStyleSheet("#infoLabel{background-color:transparent; border:transparent;}")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Dashboard"))
        self.showReviewButton.setText(_translate("Dashboard", "SHOW REVIEWS"))
        self.showScoreButton.setText(_translate("Dashboard", "SHOW SCORES"))
        self.compareButton.setText(_translate("Dashboard", "COMPARE"))
        self.analysisButton.setText(_translate("Dashboard", "SHOW ANALYSIS"))

        # our stuff
        asins=["B01LW9P0H4","B01M7O431L","B06Y15G61T","B06Y137TLR","B071WDBTW1","B079JSZ1Z2","B079SGQNPN","B079YM4RXS"]
        asin = Asin.getAsinValue()
        algo.summaryFunction(asin)
        name = Asin.getPhoneName(asin)
        print(name)
        if asin not in asins:
           image.img(asin)
        self.setContent(asin,name)

        self.showReviewButton.clicked.connect(self.showReview)
        self.showScoreButton.clicked.connect(self.showScore)
        self.compareButton.clicked.connect(self.showCompare)
        self.analysisButton.clicked.connect(self.showAnalysis)

    # our function
    def setContent(self,asin,name):
        self.picLabel.setStyleSheet("#picLabel{border-image:url(images/"+asin+".jpg)}")
        self.infoLabel.append("Product Name : \n "+name)
        self.infoLabel.append("ASIN : \n "+str(asin))

    def showReview(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_ReviewsWindow()
        self.ui.setupUi(self.window)
        self.window.show()  # open new window

    def showScore(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_ScoreWindow()
        self.ui.setupUi(self.window)
        self.window.show()  # open new window

    def showCompare(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_CompareWindow()
        self.ui.setupUi(self.window)
        self.window.show()  # open new window

    def showAnalysis(self):
        self.window = QtWidgets.QMainWindow()  # new window
        self.ui = Ui_AnalysisWindow()
        self.ui.setupUi(self.window)
        self.window.show()  # open new window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
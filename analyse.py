from PyQt5 import QtCore, QtGui, QtWidgets
import Asin
import algo
import WordCloud

class Ui_AnalysisWindow(object):
    def setupUi(self, AnalysisWindow):
        AnalysisWindow.setObjectName("AnalysisWindow")
        AnalysisWindow.resize(1366, 768)
        AnalysisWindow.setWindowIcon(QtGui.QIcon('images/analyse.png'))
        AnalysisWindow.setStyleSheet("#AnalysisWindow { border-image: url(images/img.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(AnalysisWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 0, 20, 690))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(900, 0, 20, 690))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 100, 351, 441))
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.listWidget.setFont(font)
        self.listWidget.setSpacing(4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 570, 120, 85))
        self.label_2.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.relevancyAccuracyLabel = QtWidgets.QLabel(self.centralwidget)
        self.relevancyAccuracyLabel.setGeometry(QtCore.QRect(240, 590, 160, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.relevancyAccuracyLabel.setFont(font)
        self.relevancyAccuracyLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.relevancyAccuracyLabel.setText("")
        self.relevancyAccuracyLabel.setObjectName("relevancyAccuracyLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 350, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1000, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(930, 150, 400, 300))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.prod_rating = QtWidgets.QLabel(self.centralwidget)
        self.prod_rating.setGeometry(QtCore.QRect(680, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.prod_rating.setFont(font)
        self.prod_rating.setFrameShape(QtWidgets.QFrame.Box)
        self.prod_rating.setText("")
        self.prod_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.prod_rating.setObjectName("prod_rating")
        self.ama_rating = QtWidgets.QLabel(self.centralwidget)
        self.ama_rating.setGeometry(QtCore.QRect(680, 350, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.ama_rating.setFont(font)
        self.ama_rating.setFrameShape(QtWidgets.QFrame.Box)
        self.ama_rating.setText("")
        self.ama_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.ama_rating.setObjectName("ama_rating")
        AnalysisWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AnalysisWindow)
        self.statusbar.setObjectName("statusbar")
        AnalysisWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AnalysisWindow)
        QtCore.QMetaObject.connectSlotsByName(AnalysisWindow)

    def retranslateUi(self, AnalysisWindow):
        _translate = QtCore.QCoreApplication.translate
        AnalysisWindow.setWindowTitle(_translate("AnalysisWindow", "Analysis"))
        self.label.setText(_translate("AnalysisWindow", "Feature Relevancy"))
        self.label_2.setText(_translate("AnalysisWindow", "Accuracy of relevant features extracted"))
        self.label_3.setText(_translate("AnalysisWindow", "Score Comparision"))
        self.label_4.setText(_translate("AnalysisWindow", "Our Rating"))
        self.label_5.setText(_translate("AnalysisWindow", "Amazon Rating"))
        self.label_6.setText(_translate("AnalysisWindow", "Word Cloud"))

        #our stuff
        asin=Asin.getAsinValue()
        WordCloud.wc()
        self.label_7.setStyleSheet("#label_7{border-image:url(images/"+asin+"_wc.png)}")


        from collections import defaultdict
        key_rating_d = algo.noun_dict()
        objects = key_rating_d.keys()
        performance = []

        for l in key_rating_d.values():
            for i in l:
                # print(i)
                s = i.split('/')
                performance.append(float(s[0]))
        # print(performance)
        sum=0

        for pi in performance:
            sum = sum + pi
        avg = sum/len(performance)
        avg/=2
        # print("old avg:")
        # print(avg)
        phone_word_rating = Asin.getPhone()
        # print("phone:" + str(phone_word_rating))
        new_avg = (avg + phone_word_rating / 2) / 2
        # print("new avg:")
        # print(new_avg)

        Asin.set_Prod_avg(round(new_avg, 2))
        Asin.set_Ama_avg(asin)

        amazon_rating =  Asin.get_Amazon_avg()
        product_rating = Asin.get_Prod_avg()
        # print(amazon_rating,product_rating)
        self.ama_rating.setText(str(amazon_rating))
        self.prod_rating.setText(str(product_rating))

        relcount = 0
        i=1
        for obj in objects:
            relevancy = Asin.check(str(obj))
            if relevancy == 'relevant':
                relcount += 1
            # print(str(obj), relevancy)
            self.listWidget.addItem(str(i)+". "+str(obj)+" \t : \t"+str(relevancy))
            i+=1
        rele = str(round((relcount / len(objects)),2) * 100)
        rel=rele+"%"
        self.relevancyAccuracyLabel.setText(rel)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalysisWindow = QtWidgets.QMainWindow()
    ui = Ui_AnalysisWindow()
    ui.setupUi(AnalysisWindow)
    AnalysisWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 340, 651, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.commentLabel = QtWidgets.QLabel(self.groupBox)
        self.commentLabel.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentLabel.setFont(font)
        self.commentLabel.setObjectName("commentLabel")
        self.userComment = QtWidgets.QLineEdit(self.groupBox)
        self.userComment.setGeometry(QtCore.QRect(120, 90, 261, 61))
        self.userComment.setObjectName("userComment")
        self.postLabel = QtWidgets.QLabel(self.groupBox)
        self.postLabel.setGeometry(QtCore.QRect(30, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.postLabel.setFont(font)
        self.postLabel.setObjectName("postLabel")
        self.numOfPostsToTarget = QtWidgets.QLineEdit(self.groupBox)
        self.numOfPostsToTarget.setEnabled(True)
        self.numOfPostsToTarget.setGeometry(QtCore.QRect(230, 30, 198, 30))
        font = QtGui.QFont()
        font.setKerning(True)
        self.numOfPostsToTarget.setFont(font)
        self.numOfPostsToTarget.setAutoFillBackground(False)
        self.numOfPostsToTarget.setObjectName("numOfPostsToTarget")
        self.exploreBtn = QtWidgets.QToolButton(self.centralwidget)
        self.exploreBtn.setGeometry(QtCore.QRect(60, 80, 81, 71))
        self.exploreBtn.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"alternate-background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-color: rgb(240, 240, 240);")
        self.exploreBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("compass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exploreBtn.setIcon(icon1)
        self.exploreBtn.setIconSize(QtCore.QSize(120, 120))
        self.exploreBtn.setCheckable(False)
        self.exploreBtn.setObjectName("exploreBtn")
        self.hashtagBtn = QtWidgets.QToolButton(self.centralwidget)
        self.hashtagBtn.setGeometry(QtCore.QRect(170, 80, 81, 71))
        self.hashtagBtn.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"alternate-background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-color: rgb(240, 240, 240);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("hashtag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hashtagBtn.setIcon(icon2)
        self.hashtagBtn.setIconSize(QtCore.QSize(120, 120))
        self.hashtagBtn.setObjectName("hashtagBtn")
        self.followFollowerBtn = QtWidgets.QToolButton(self.centralwidget)
        self.followFollowerBtn.setGeometry(QtCore.QRect(280, 80, 101, 71))
        self.followFollowerBtn.setAutoFillBackground(False)
        self.followFollowerBtn.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"alternate-background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"border-color: rgb(240, 240, 240);")
        def getComment(self):
            comment = self.userComment
            self.windowTitle = comment
            self.windowTitle.setText("MainWindow", comment)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("not-compatible.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.followFollowerBtn.setIcon(icon3)
        self.followFollowerBtn.setIconSize(QtCore.QSize(120, 120))
        self.followFollowerBtn.setObjectName("followFollowerBtn")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(640, 610, 111, 31))
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(getComment)

        self.windowTitle = QtWidgets.QLabel(self.centralwidget)
        self.windowTitle.setGeometry(QtCore.QRect(50, 0, 158, 78))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.windowTitle.setFont(font)
        self.windowTitle.setObjectName("windowTitle")
        self.exploreBtnLabel = QtWidgets.QLabel(self.centralwidget)
        self.exploreBtnLabel.setGeometry(QtCore.QRect(80, 160, 47, 13))
        self.exploreBtnLabel.setObjectName("exploreBtnLabel")
        self.hashtagBtnLabel = QtWidgets.QLabel(self.centralwidget)
        self.hashtagBtnLabel.setGeometry(QtCore.QRect(190, 160, 47, 13))
        self.hashtagBtnLabel.setObjectName("hashtagBtnLabel")
        self.followFollowerBtnLabel = QtWidgets.QLabel(self.centralwidget)
        self.followFollowerBtnLabel.setGeometry(QtCore.QRect(270, 160, 111, 16))
        self.followFollowerBtnLabel.setObjectName("followFollowerBtnLabel")
        self.exploreDesc = QtWidgets.QLabel(self.centralwidget)
        self.exploreDesc.setGeometry(QtCore.QRect(60, 196, 601, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exploreDesc.setFont(font)
        self.exploreDesc.setObjectName("exploreDesc")
        self.hashtagDesc = QtWidgets.QLabel(self.centralwidget)
        self.hashtagDesc.setGeometry(QtCore.QRect(60, 230, 591, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hashtagDesc.setFont(font)
        self.hashtagDesc.setObjectName("hashtagDesc")
        self.followersDesc = QtWidgets.QLabel(self.centralwidget)
        self.followersDesc.setGeometry(QtCore.QRect(60, 260, 851, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.followersDesc.setFont(font)
        self.followersDesc.setObjectName("followersDesc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "INFO"))
        self.commentLabel.setText(_translate("MainWindow", "Comment:"))
        self.postLabel.setText(_translate("MainWindow", "Number of Posts to target:"))
        self.hashtagBtn.setText(_translate("MainWindow", "..."))
        self.followFollowerBtn.setText(_translate("MainWindow", "..."))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.windowTitle.setText(_translate("MainWindow", "Instagram Bot"))
        self.exploreBtnLabel.setText(_translate("MainWindow", "Explore"))
        self.hashtagBtnLabel.setText(_translate("MainWindow", "Hashtag"))
        self.followFollowerBtnLabel.setText(_translate("MainWindow", "Followers & Following"))
        self.exploreDesc.setText(_translate("MainWindow", "Explore - likes & comments on posts that are in the EXPLORE page."))
        self.hashtagDesc.setText(_translate("MainWindow", "Hashtag - likes & comments on posts that are under a SPECIFIC HASHTAG."))
        self.followersDesc.setText(_translate("MainWindow", "Followers & Following - find out who you are following. Who are your followers,\n"
"and who is NOT following you back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

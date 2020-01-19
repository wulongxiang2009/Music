# Music
免费下载网易音乐的下载器，界面由qt designer生成！作者微信号：wulongxiang2009,欢迎交流！
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wangyi.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
# 
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 447)
        MainWindow.setStyleSheet("QPushButton:pressed {\n"
                                 "    background-color: rgb(0, 0, 0);\n"
                                 "    border-style: inset;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 671, 451))
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
                                     "    alignment: left;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:hover {\n"
                                     "    background: #68668f;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    border-color: #3a3a3f;\n"
                                     "    color: #dcdde4;\n"
                                     "    border-bottom-color: #5c3de4;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab {\n"
                                     "    background: #000ff000;\n"
                                     "    border: none;\n"
                                     "    border-bottom: 2px solid #3c3e42;\n"
                                     "    min-width: 10px;\n"
                                     "    margin-right: 8px;\n"
                                     "    padding-left: 20px;\n"
                                     "    padding-right: 20px;\n"
                                     "    padding-top: 10px;\n"
                                     "    padding-bottom: 10px;\n"
                                     "    color: #86a6e6;\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.wangyitab = QtWidgets.QWidget()
        self.wangyitab.setObjectName("wangyitab")
        self.layoutWidget = QtWidgets.QWidget(self.wangyitab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.songlabel = QtWidgets.QLabel(self.layoutWidget)
        self.songlabel.setStyleSheet("border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.songlabel.setObjectName("songlabel")
        self.horizontalLayout.addWidget(self.songlabel)
        self.songedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.songedit.setMinimumSize(QtCore.QSize(62, 31))
        self.songedit.setMaximumSize(QtCore.QSize(480, 31))
        self.songedit.setStyleSheet("border-style:none;\n"
                                    "padding:11px;\n"
                                    "border-radius:3px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:2px solid #3a3a3f;\n"
                                    "border-right:2px solid #3a3a3f;\n"
                                    "border-left:2px solid #3a3a3f;\n"
                                    "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: 13pt \".SF NS Text\";\n"
                                    "color: rgb(174, 0, 60);\n"
                                    "")
        self.songedit.setObjectName("songedit")
        self.horizontalLayout.addWidget(self.songedit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.songlist = QtWidgets.QListWidget(self.layoutWidget)
        self.songlist.setStyleSheet("border-style:none;\n"
                                    "padding:11px;\n"
                                    "border-radius:3px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:2px solid #3a3a3f;\n"
                                    "border-right:2px solid #3a3a3f;\n"
                                    "border-left:2px solid #3a3a3f;\n"
                                    "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: 13pt \".SF NS Text\";\n"
                                    "color: rgb(9, 13, 12);")
        self.songlist.setObjectName("songlist")
        self.verticalLayout.addWidget(self.songlist)
        self.pathedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pathedit.setStyleSheet("border-style:none;\n"
                                    "padding:11px;\n"
                                    "border-radius:3px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:2px solid #3a3a3f;\n"
                                    "border-right:2px solid #3a3a3f;\n"
                                    "border-left:2px solid #3a3a3f;\n"
                                    "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: 13pt \".SF NS Text\";\n"
                                    "color: rgb(174, 0, 60);")
        self.pathedit.setObjectName("pathedit")
        self.verticalLayout.addWidget(self.pathedit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnsave = QtWidgets.QPushButton(self.layoutWidget)
        self.btnsave.setMinimumSize(QtCore.QSize(62, 45))
        self.btnsave.setMaximumSize(QtCore.QSize(120, 45))
        self.btnsave.setStyleSheet("border-style:none;\n"
                                   "border-radius:8px;\n"
                                   "background:transparent;\n"
                                   "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                   "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                   "border-top:2px solid #3a3a3f;\n"
                                   "border-right:2px solid #3a3a3f;\n"
                                   "border-left:2px solid #3a3a3f;\n"
                                   "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 13pt \".SF NS Text\";")
        self.btnsave.setObjectName("btnsave")
        self.horizontalLayout_2.addWidget(self.btnsave)
        self.btnstart = QtWidgets.QPushButton(self.layoutWidget)
        self.btnstart.setMinimumSize(QtCore.QSize(62, 45))
        self.btnstart.setMaximumSize(QtCore.QSize(111, 45))
        self.btnstart.setStyleSheet("border-style:none;\n"
                                    "border-radius:8px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:2px solid #3a3a3f;\n"
                                    "border-right:2px solid #3a3a3f;\n"
                                    "border-left:2px solid #3a3a3f;\n"
                                    "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: 13pt \".SF NS Text\";")
        self.btnstart.setObjectName("btnstart")
        self.horizontalLayout_2.addWidget(self.btnstart)
        self.btnexit = QtWidgets.QPushButton(self.layoutWidget)
        self.btnexit.setMinimumSize(QtCore.QSize(62, 45))
        self.btnexit.setMaximumSize(QtCore.QSize(113, 45))
        self.btnexit.setStyleSheet("border-style:none;\n"
                                   "border-radius:8px;\n"
                                   "background:transparent;\n"
                                   "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                   "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                   "border-top:2px solid #3a3a3f;\n"
                                   "border-right:2px solid #3a3a3f;\n"
                                   "border-left:2px solid #3a3a3f;\n"
                                   "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 13pt \".SF NS Text\";")
        self.btnexit.setObjectName("btnexit")
        self.horizontalLayout_2.addWidget(self.btnexit)
        self.btnabout = QtWidgets.QPushButton(self.layoutWidget)
        self.btnabout.setMinimumSize(QtCore.QSize(62, 45))
        self.btnabout.setMaximumSize(QtCore.QSize(113, 45))
        self.btnabout.setStyleSheet("border-style:none;\n"
                                    "border-radius:8px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:2px solid #3a3a3f;\n"
                                    "border-right:2px solid #3a3a3f;\n"
                                    "border-left:2px solid #3a3a3f;\n"
                                    "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: 13pt \".SF NS Text\";")
        self.btnabout.setObjectName("btnabout")
        self.horizontalLayout_2.addWidget(self.btnabout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.wangyitab, "")
        self.QQtab = QtWidgets.QWidget()
        self.QQtab.setObjectName("QQtab")
        self.layoutWidget1 = QtWidgets.QWidget(self.QQtab)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 661, 401))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.songlabelqq = QtWidgets.QLabel(self.layoutWidget1)
        self.songlabelqq.setStyleSheet("border-style:none;\n"
                                       "border-radius:6px;\n"
                                       "background:transparent;\n"
                                       "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                       "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                       "border-top:1px solid #3a3a3f;\n"
                                       "border-right:1px solid #3a3a3f;\n"
                                       "border-left:1px solid #3a3a3f;")
        self.songlabelqq.setObjectName("songlabelqq")
        self.horizontalLayout_3.addWidget(self.songlabelqq)
        self.songeditqq = QtWidgets.QLineEdit(self.layoutWidget1)
        self.songeditqq.setMinimumSize(QtCore.QSize(62, 31))
        self.songeditqq.setMaximumSize(QtCore.QSize(480, 31))
        self.songeditqq.setStyleSheet("border-style:none;\n"
                                      "padding:11px;\n"
                                      "border-radius:3px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:2px solid #3a3a3f;\n"
                                      "border-right:2px solid #3a3a3f;\n"
                                      "border-left:2px solid #3a3a3f;\n"
                                      "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: 13pt \".SF NS Text\";")
        self.songeditqq.setObjectName("songeditqq")
        self.horizontalLayout_3.addWidget(self.songeditqq)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.songlistqq = QtWidgets.QListWidget(self.layoutWidget1)
        self.songlistqq.setStyleSheet("border-style:none;\n"
                                      "padding:11px;\n"
                                      "border-radius:3px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:2px solid #3a3a3f;\n"
                                      "border-right:2px solid #3a3a3f;\n"
                                      "border-left:2px solid #3a3a3f;\n"
                                      "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: 13pt \".SF NS Text\";")
        self.songlistqq.setObjectName("songlistqq")
        self.verticalLayout_2.addWidget(self.songlistqq)
        self.patheditqq = QtWidgets.QLineEdit(self.layoutWidget1)
        self.patheditqq.setStyleSheet("border-style:none;\n"
                                      "padding:11px;\n"
                                      "border-radius:3px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:2px solid #3a3a3f;\n"
                                      "border-right:2px solid #3a3a3f;\n"
                                      "border-left:2px solid #3a3a3f;\n"
                                      "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: 13pt \".SF NS Text\";")
        self.patheditqq.setObjectName("patheditqq")
        self.verticalLayout_2.addWidget(self.patheditqq)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnsaveqq = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnsaveqq.setMinimumSize(QtCore.QSize(62, 45))
        self.btnsaveqq.setMaximumSize(QtCore.QSize(111, 45))
        self.btnsaveqq.setStyleSheet("border-style:none;\n"
                                     "padding:11px;\n"
                                     "border-radius:3px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:2px solid #3a3a3f;\n"
                                     "border-right:2px solid #3a3a3f;\n"
                                     "border-left:2px solid #3a3a3f;\n"
                                     "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "font: 13pt \".SF NS Text\";")
        self.btnsaveqq.setObjectName("btnsaveqq")
        self.horizontalLayout_4.addWidget(self.btnsaveqq)
        self.btnstartqq = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnstartqq.setMinimumSize(QtCore.QSize(62, 45))
        self.btnstartqq.setMaximumSize(QtCore.QSize(111, 45))
        self.btnstartqq.setStyleSheet("border-style:none;\n"
                                      "padding:11px;\n"
                                      "border-radius:3px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:2px solid #3a3a3f;\n"
                                      "border-right:2px solid #3a3a3f;\n"
                                      "border-left:2px solid #3a3a3f;\n"
                                      "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: 13pt \".SF NS Text\";")
        self.btnstartqq.setObjectName("btnstartqq")
        self.horizontalLayout_4.addWidget(self.btnstartqq)
        self.btnexitqq = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnexitqq.setMinimumSize(QtCore.QSize(62, 45))
        self.btnexitqq.setMaximumSize(QtCore.QSize(113, 45))
        self.btnexitqq.setStyleSheet("border-style:none;\n"
                                     "padding:11px;\n"
                                     "border-radius:3px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:2px solid #3a3a3f;\n"
                                     "border-right:2px solid #3a3a3f;\n"
                                     "border-left:2px solid #3a3a3f;\n"
                                     "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "font: 13pt \".SF NS Text\";")
        self.btnexitqq.setObjectName("btnexitqq")
        self.horizontalLayout_4.addWidget(self.btnexitqq)
        self.btnaboutqq = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnaboutqq.setMinimumSize(QtCore.QSize(62, 45))
        self.btnaboutqq.setMaximumSize(QtCore.QSize(113, 45))
        self.btnaboutqq.setStyleSheet("border-style:none;\n"
                                      "padding:11px;\n"
                                      "border-radius:3px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 2px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:2px solid #3a3a3f;\n"
                                      "border-right:2px solid #3a3a3f;\n"
                                      "border-left:2px solid #3a3a3f;\n"
                                      "border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(50, 16, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: 13pt \".SF NS Text\";")
        self.btnaboutqq.setObjectName("btnaboutqq")
        self.horizontalLayout_4.addWidget(self.btnaboutqq)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.QQtab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.songlabel.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#f200f0;\">请输入下载的歌曲名：</span></p></body></html>"))
        self.songedit.setText(_translate("MainWindow", "如：电灯胆"))
        self.pathedit.setText(_translate("MainWindow", "点击[选择文件夹]选择歌曲保存路径："))
        self.btnsave.setText(_translate("MainWindow", "选择文件夹"))
        self.btnstart.setText(_translate("MainWindow", "开始下载"))
        self.btnexit.setText(_translate("MainWindow", "退出程序"))
        self.btnabout.setText(_translate("MainWindow", "关于作者"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wangyitab), _translate("MainWindow", "网易音乐"))
        self.songlabelqq.setText(_translate("MainWindow", "请输入下载的歌曲名："))
        self.btnsaveqq.setText(_translate("MainWindow", "保存路径"))
        self.btnstartqq.setText(_translate("MainWindow", "开始下载"))
        self.btnexitqq.setText(_translate("MainWindow", "退出程序"))
        self.btnaboutqq.setText(_translate("MainWindow", "关于作者"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.QQtab), _translate("MainWindow", "QQ音乐"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailReaderUiv2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 195)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.readfileButton_1 = QtWidgets.QPushButton(Form)
        self.readfileButton_1.setGeometry(QtCore.QRect(460, 30, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readfileButton_1.sizePolicy().hasHeightForWidth())
        self.readfileButton_1.setSizePolicy(sizePolicy)
        self.readfileButton_1.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.readfileButton_1.setSizeIncrement(QtCore.QSize(0, 0))
        self.readfileButton_1.setBaseSize(QtCore.QSize(0, 0))
        self.readfileButton_1.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.readfileButton_1.setObjectName("readfileButton_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 321, 21))
        self.lineEdit.setStyleSheet("QLineEdit{border: 1px solid gray;border-radius: 3px;background:rgb(255,250,240); font: 10pt \"苹方 粗体\"; } QLineEdit:hover{border-color:transparent; }\n"
"\n"
"   ")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_2.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 321, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit{border: 1px solid gray;border-radius: 3px;background:rgb(255,250,240); \n"
"font: 10pt \"苹方 粗体\"; } QLineEdit:hover{border-color:transparent; }\n"
"   ")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.readfileButton_2 = QtWidgets.QPushButton(Form)
        self.readfileButton_2.setGeometry(QtCore.QRect(460, 70, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readfileButton_2.sizePolicy().hasHeightForWidth())
        self.readfileButton_2.setSizePolicy(sizePolicy)
        self.readfileButton_2.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.readfileButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.readfileButton_2.setBaseSize(QtCore.QSize(0, 0))
        self.readfileButton_2.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.readfileButton_2.setObjectName("readfileButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 110, 61, 16))
        self.label_3.setStyleSheet("\n"
"font: 10pt \"苹方 粗体\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 110, 211, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit{border: 1px solid gray;border-radius: 3px;background:rgb(255,250,240); \n"
"font: 10pt \"苹方 粗体\"; } QLineEdit:hover{border-color:transparent; }\n"
"   ")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.readfileButton_3 = QtWidgets.QPushButton(Form)
        self.readfileButton_3.setGeometry(QtCore.QRect(510, 110, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readfileButton_3.sizePolicy().hasHeightForWidth())
        self.readfileButton_3.setSizePolicy(sizePolicy)
        self.readfileButton_3.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.readfileButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.readfileButton_3.setBaseSize(QtCore.QSize(0, 0))
        self.readfileButton_3.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.readfileButton_3.setObjectName("readfileButton_3")
        self.startTrainButton = QtWidgets.QPushButton(Form)
        self.startTrainButton.setGeometry(QtCore.QRect(250, 150, 93, 28))
        self.startTrainButton.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.startTrainButton.setObjectName("startTrainButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 91, 16))
        self.label_4.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 210, 331, 21))
        self.lineEdit_4.setStyleSheet("QLineEdit{border: 1px solid gray;border-radius: 3px;background:rgb(255,250,240); \n"
"font: 10pt \"苹方 粗体\"; } QLineEdit:hover{border-color:transparent; }\n"
"   ")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.readfileButton_4 = QtWidgets.QPushButton(Form)
        self.readfileButton_4.setGeometry(QtCore.QRect(460, 210, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readfileButton_4.sizePolicy().hasHeightForWidth())
        self.readfileButton_4.setSizePolicy(sizePolicy)
        self.readfileButton_4.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.readfileButton_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.readfileButton_4.setBaseSize(QtCore.QSize(0, 0))
        self.readfileButton_4.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.readfileButton_4.setObjectName("readfileButton_4")
        self.startTestButton = QtWidgets.QPushButton(Form)
        self.startTestButton.setGeometry(QtCore.QRect(250, 260, 93, 28))
        self.startTestButton.setStyleSheet("border: 2px solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);     \n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}  \n"
"QPushButton:pressed{border-color:gray}        \n"
"")
        self.startTestButton.setObjectName("startTestButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 110, 81, 21))
        self.comboBox.setStyleSheet("border: 2px  solid grey;   \n"
"font: 10pt \"苹方 粗体\";\n"
"background:rgb(255,250,240);\n"
"border-radius: 8px;  \n"
"hover{border-color:rgb(183,203,188);}       \n"
"  \n"
"\n"
"        \n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_5.setStyleSheet("\n"
"font: 10pt \"苹方 粗体\";")
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 270, 415, 301))
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 30, 130, 242))
        self.scrollArea.setMaximumSize(QtCore.QSize(130, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 152, 242))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spamWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.spamWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spamWidget.sizePolicy().hasHeightForWidth())
        self.spamWidget.setSizePolicy(sizePolicy)
        self.spamWidget.setMinimumSize(QtCore.QSize(130, 220))
        self.spamWidget.setObjectName("spamWidget")
        self.spamListWidget = QtWidgets.QListWidget(self.spamWidget)
        self.spamListWidget.setEnabled(True)
        self.spamListWidget.setGeometry(QtCore.QRect(0, 0, 108, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spamListWidget.sizePolicy().hasHeightForWidth())
        self.spamListWidget.setSizePolicy(sizePolicy)
        self.spamListWidget.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.spamListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spamListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.spamListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.spamListWidget.setAutoScroll(True)
        self.spamListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.spamListWidget.setObjectName("spamListWidget")
        self.hamListWidget = QtWidgets.QListWidget(self.spamWidget)
        self.hamListWidget.setEnabled(True)
        self.hamListWidget.setGeometry(QtCore.QRect(0, 110, 108, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hamListWidget.sizePolicy().hasHeightForWidth())
        self.hamListWidget.setSizePolicy(sizePolicy)
        self.hamListWidget.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.hamListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hamListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hamListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hamListWidget.setAutoScroll(True)
        self.hamListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.hamListWidget.setObjectName("hamListWidget")
        self.verticalLayout.addWidget(self.spamWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 40, 251, 231))
        self.textBrowser.setStyleSheet("font: 10pt \"苹方 粗体\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.readfileButton_1.setText(_translate("Form", "选择文件夹"))
        self.label.setText(_translate("Form", "spam训练集:"))
        self.label_2.setText(_translate("Form", "ham训练集："))
        self.readfileButton_2.setText(_translate("Form", "选择文件夹"))
        self.label_3.setText(_translate("Form", "分词集："))
        self.readfileButton_3.setText(_translate("Form", "选择文件"))
        self.startTrainButton.setText(_translate("Form", "开始训练"))
        self.label_4.setText(_translate("Form", "测试邮件集："))
        self.readfileButton_4.setText(_translate("Form", "选择文件夹"))
        self.startTestButton.setText(_translate("Form", "开始测试"))
        self.comboBox.setItemText(0, _translate("Form", "贝叶斯"))
        self.comboBox.setItemText(1, _translate("Form", "KNN"))
        self.label_5.setText(_translate("Form", "训练算法选择："))


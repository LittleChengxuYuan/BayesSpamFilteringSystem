# a mail reader gui program

# Todo: 1.从txt文件中读取邮件
# Todo: 2.从outlook邮箱中读取邮件
# Todo: 3.对邮件内容进行spam/ham判别
# Todo: 4.读取文件夹（2个 ham训练集 spam训练集 ） 读取文件路径 （分词文件）

import re
import sys
import os
import os.path
from MailReader.mailReaderUiv2 import Ui_Form

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget,QLineEdit,QListWidget,QMessageBox,QProgressDialog
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import Preprocess

class MailReaderMain(QMainWindow,Ui_Form,QListWidget):
    def __init__(self):
        super().__init__()
        self.algorithm='bayes'
        self.spamPath=''
        self.hamPath=''
        self.splitData=''
        self.emailPath=''

        self.spamitemNum=0
        self.hamitemNum=0
        self.trainResult=''

        self.setupUi(self)
        self.readfileButton_1.clicked.connect(self.btn_1_read_clicked)
        self.readfileButton_2.clicked.connect(self.btn_2_read_clicked)
        self.readfileButton_3.clicked.connect(self.btn_3_read_clicked)
        self.readfileButton_4.clicked.connect(self.btn_4_read_clicked)

        self.startTrainButton.clicked.connect(self.startTrainButtonClicked)
        self.startTestButton.clicked.connect(self.startTestButtonClicked)
        self.spamListWidget.itemClicked.connect(self.myItemClicked)
        self.hamListWidget.itemClicked.connect(self.myItemClicked)
        if(self.comboBox.currentText=='贝叶斯'):
            self.algorithm='bayes'
        elif(self.comboBox.currentText=='KNN'):
            self.algorithm='KNN'
        self.show()

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在训练...")

        progress.setMinimumDuration(3)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")

    def btn_1_read_clicked(self):
        filepath=QFileDialog.getExistingDirectory(self,'' ,'X:\\documents\\数据挖掘\\email\\email')
        self.spamPath=filepath
        self.lineEdit.setText(self.spamPath)
        # files = os.listdir(self.spamPath)
        # for name in files:
        #     for ext in ".txt":
        #         if (name.endswith(ext)):
        #             print(name)
        #             break



    def btn_2_read_clicked(self):
        filepath = QFileDialog.getExistingDirectory(self, '', 'X:\\documents\\数据挖掘\\email\\email')
        self.hamPath = filepath
        self.lineEdit_2.setText(self.hamPath)

    def btn_3_read_clicked(self):
        filename = QFileDialog.getOpenFileName(self, '', 'X:\\programs\\python\\BayesSpamFilteringSystem\\stopwords')
        self.splitData = filename[0]
        self.lineEdit_3.setText(self.splitData)

    def btn_4_read_clicked(self):
        filepath=QFileDialog.getExistingDirectory(self,'','X:\\documents\\数据挖掘\\email\\email')
        self.emailPath=filepath
        self.lineEdit_4.setText(self.emailPath)





    # def btn_readname(self):
    #     self.spamListWidget.clear()
    #     self.itemNum=0
    #     filepath=QFileDialog.getExistingDirectory(self,'', 'X:\\documents\\数据挖掘\\email\\email')
    #     files=os.listdir(filepath)
    #     for name in files:
    #         if(name.endswith(".txt")):
    #             self.itemNum+=1
    #             self.spamListWidget.addItem(name+" spam")
    #     print (self.itemNum)
    #     #重新设置窗体大小
    #     controlHeight=self.itemNum*26
    #     self.spamListWidget.setGeometry(QtCore.QRect(0,0,110,controlHeight))
    #     self.spamWidget.setMinimumSize(130,controlHeight)
    #
    #     #self.listWidget.setGeometry(QtCore.QRect(50,211,51,220))
    #     self.spamListWidget.itemClicked.connect(self.myItemClicked)

    def myItemClicked(self,item):
        self.textBrowser.clear()
        spaceIndex=str(item.text()).rstrip(' spamh')
        # spaceIndex=[m.start() for m in re.finditer(' ',str(item.text()))]
        # spaceIndex=str(spaceIndex)
        filename=self.emailPath+'\\'+spaceIndex
        #print(filename)
        thetext=open(filename).read()
        self.textBrowser.setPlainText(thetext)
        #print (spaceIndex)

    def startTrainButtonClicked(self):
        self.trainResult=Preprocess.Preprocess(self.hamPath,self.spamPath,self.splitData)
        self.resize(612,560)
        self.setMaximumSize(612,560)

        # trainResult=Preprocess.Preprocess(self.hamPath,self.spamPath,self.splitData)

        # result=trainResult.getResult_1(self.algorithm,'X:\\zTimDownload\\email\\email\\ham\\1.txt')
        # self.textBrowser.setPlainText(open('X:\\zTimDownload\\email\\email\\ham\\1.txt').read())
        # print(result)
        #print(self.hamPath+self.spamPath+self.splitData)

    def startTestButtonClicked(self):
        self.startTestButton.setEnabled(False)
        for parent,dirnames,filenames, in os.walk(self.emailPath):
            for filename in filenames:
                thefile=os.path.join(parent,filename)
                result=self.trainResult.getResult_1(self.algorithm,thefile)
                if result==0:
                    self.spamListWidget.addItem(filename+" spam")
                    self.spamitemNum+=1
                elif result==1:
                    self.hamListWidget.addItem(filename+" ham")
                    self.hamitemNum+=1

        spamHeight = self.spamitemNum * 26
        self.spamListWidget.setGeometry(QtCore.QRect(0, 0, 110, spamHeight))
        hamHeight = self.hamitemNum * 26
        self.hamListWidget.setGeometry(QtCore.QRect(0, spamHeight, 110, hamHeight))
        controlHeight=self.hamitemNum*26+self.spamitemNum*26
        self.spamWidget.setMinimumSize(130, controlHeight)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MailReaderMain()
    sys.exit(app.exec_())






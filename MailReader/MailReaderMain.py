# a mail reader gui program

# Todo: 1.从txt文件中读取邮件
# Todo: 2.从outlook邮箱中读取邮件
# Todo: 3.对邮件内容进行spam/ham判别
# Todo: 4.读取文件夹（2个 ham训练集 spam训练集 ） 读取文件路径 （分词文件）

import sys
from MailReader.mailReaderUiv2 import Ui_Form

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget,QLineEdit
from PyQt5.QtCore import QDir,pyqtSignal


class MailReaderMain(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()

        self.spamPath=''
        self.hamPath=''
        self.splitData=''
        self.setupUi(self)
        self.readfileButton_1.clicked.connect(self.btn_1_read_clicked)
        self.readfileButton_2.clicked.connect(self.btn_2_read_clicked)
        #self.pushButton.clicked.connect(self.btn_read_clicked)
        self.show()

    def btn_1_read_clicked(self):
        filepath=QFileDialog.getExistingDirectory(self,'' ,'X:\\documents\\数据挖掘\\email\\email')
        self.spamPath=filepath
        self.lineEdit.setText(self.spamPath)

    def btn_2_read_clicked(self):
        filepath = QFileDialog.getExistingDirectory(self, '', 'X:\\documents\\数据挖掘\\email\\email')
        self.hamPath = filepath
        self.lineEdit_2.setText(self.hamPath)

    def btn_3_read_clicked(self):
        filepath = QFileDialog.getExistingDirectory(self, '', 'X:\\documents\\数据挖掘\\email\\email')
        self.splitData = filepath
        self.lineEdit_3.setText(self.spamPath)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MailReaderMain()
    sys.exit(app.exec_())






from sklearn import svm
import numpy as np
from openpyxl import Workbook
import csv

# 根据SVM函数特性编码，针对每一篇短文获取频率最高的十五单词，将其保存在
class MySVM:
    def getResult(self,testDict,spamDict,hamDict,spamFileNum,hamFileNum):
        newspam = sorted(spamDict.keys(),key=lambda d:d[1],reverse=True)[0:int(len(spamDict)/2)]
        # newham = sorted(hamDict.items(),key=lambda d:d[1],reverse=True)[0,14]
        # print(newspam)
        print(len(newspam))
        wb = Workbook()
        sheet = wb.active

        print(newspam)
        return 0
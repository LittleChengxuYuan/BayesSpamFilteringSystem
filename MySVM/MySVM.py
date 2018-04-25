from sklearn import svm
import numpy as np
from openpyxl import Workbook
import openpyxl

# 根据SVM函数特性编码，针对每一篇短文获取频率最高的十五单词，将其保存在
class MySVM:
    def getResult(self,testDict,spamDict,hamDict,spamFileNum,hamFileNum):
        newspam = sorted(spamDict.items(),key=lambda d:d[1],reverse=True)[0:int(len(spamDict)/2)]
        newham = sorted(hamDict.items(),key=lambda d:d[1],reverse=True)[0:int(len(hamDict)/4)]

        print(len(newham))
        wb = Workbook()
        sheet = wb.active
        for col in range(0,len(newspam)):
            try:
                sheet.cell(1,col+1,value=newspam[col][0])
            except openpyxl.utils.exceptions.IllegalCharacterError:
                sheet.cell(1,col+1,value="unknown")
        wb.save('newSpam.xlsx')
        wb.close

        wb2 = Workbook()
        sheet2 = wb2.active
        for col in range(0,len(newham)):
            try:
                sheet2.cell(1,col+1,value=newham[col][0])
            except openpyxl.utils.exceptions.IllegalCharacterError:
                sheet2.cell(1,col+1,value="unknown")
            except:
                print("捕获未知异常")
        wb2.save('newham.xlsx')
        #print(newspam),
        return 0
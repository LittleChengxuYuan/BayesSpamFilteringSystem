from sklearn import svm
import numpy as np
from openpyxl import Workbook
import openpyxl
import os
import jieba

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
    
    def train(self,spamDict,hamDict,spamFilePath,hamFilePath):
        newspam = sorted(spamDict.items(),key=lambda d:d[1],reverse=True)[0:int(len(spamDict)/2)]
        newham = sorted(hamDict.items(),key=lambda d:d[1],reverse=True)[0:int(len(hamDict)/2)]
        wordListTupe = list(set(newspam+newham))
        wordList = []
        for (k1,k2) in wordListTupe:
            wordList.append(k1)

        wb = Workbook()
        sheet = wb.active
        for row in range(0,len(wordList)):
            try:
                sheet.cell(row+2,1,value=wordList[row])
            except openpyxl.utils.exceptions.IllegalCharacterError:
                sheet.cell(row+2,1,value="unknown")
                print("异常字符")
        
        fileList = os.listdir(spamFilePath)
        

        col = 2
        for i in range(0,len(fileList)):
            fileName = fileList[i]
            wordDict={}
            file = open(spamFilePath+'/'+fileName,encoding="utf8").read()
            res_list = jieba.lcut(file)
            for i in res_list:
                if i.strip()!='' and i!=None:
                    if i in wordDict.keys():
                        wordDict[i]+=1
                    else:
                        wordDict.setdefault(i,1)
        for key,value in wordDict:
            if key in wordList:
                
        wb.save('wordList.xlsx')


    def __getWordDict(self,filePath):
        wordDict={}
        fileList = os.listdir(filePath)
        for fileName in fileList:
            file_object = open(filePath+'/'+fileName,encoding="utf8").read()
            res_list = jieba.lcut(file_object)
            for i in res_list:
                if i.strip()!='' and i!=None:
                    if i in wordDict.keys():
                        wordDict[i]+=1
                    else:
                        wordDict.setdefault(i,1)
        return wordDict    
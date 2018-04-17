from Bayes import Bayes
import os
import re

bayes = Bayes()

#保存词频的字典
hamDict = {}
spamDict = {}
testDict = {}

#分别获得正常邮件、垃圾邮件文件名称列表
hamFilePath = ("./ham")
spamFilePath = ("./spam")
testFilePath = ("./test")
hamFileList = os.listdir(hamFilePath)
spamFileList = os.listdir(spamFilePath)
testFileList = os.listdir(testFilePath)
hamFileNum = len(hamFileList)
spamFileNum = len(spamFileList)

#读取停用词表
stopList = open("./stopwords/StopWordsENG.txt").read().split()
#stopList = []
#获取正常邮件的词频
for fileName in hamFileList:
    file_object = open(hamFilePath+'/'+fileName).read()
    bayes.getWordList(file_object,hamDict,stopList)
#print(hamDict)

#获取垃圾邮件的词频
for fileName in spamFileList:
    file_object = open(spamFilePath+'/'+fileName).read()
    bayes.getWordList(file_object,spamDict,stopList)
#print(spamDict)

#获取测试邮件的内容
for fileName in testFileList:
    testFile = open(testFilePath+'/'+fileName,encoding="utf8").read()
    bayes.getWordList(testFile,testDict,stopList)
    print(fileName)
    bayes.getTestWords(testDict,spamDict,hamDict,spamFileNum,hamFileNum)
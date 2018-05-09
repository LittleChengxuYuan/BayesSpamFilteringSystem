from Preprocess import Preprocess
import os
import re
testFilePath = "./test/test-mails/ham/8-899msg1.txt"
testFileList = os.listdir(testFilePath)
preprocess = Preprocess("./test/train-mails/ham","./test/train-mails/spam","./stopwords/StopWords.txt")
isSpam = 0
for fileName in testFileList:
    #print(fileName)
    result = 0
    result = preprocess.getResult_1("bayes",testFilePath+'/'+fileName)
    if result==0:
        isSpam = isSpam + 1
print(isSpam/len(testFileList))
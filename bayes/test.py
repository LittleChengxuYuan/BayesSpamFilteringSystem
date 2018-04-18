from Bayes import Bayes
import os
import re
testFilePath = "./test/English/test-mails/ham"
testFileList = os.listdir(testFilePath)
bayes = Bayes("./test/English/train-mails/ham","./test/English/train-mails/spam","./stopwords/StopWords.txt")
isSpam = 0
for fileName in testFileList:
    #print(fileName)
    result = 0
    result = bayes.getResult(testFilePath+'/'+fileName)
    if result==0:
        isSpam = isSpam + 1
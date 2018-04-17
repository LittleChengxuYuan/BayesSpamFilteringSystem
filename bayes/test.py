from Bayes import Bayes
import os
import re
testFilePath = "./test/test-mails"
testFileList = os.listdir(testFilePath)
bayes = Bayes("./test/train-mails/ham","./test/train-mails/spam","./stopwords/StopWordsENG.txt")
for fileName in testFileList:
    print(fileName)
    bayes.getResult(testFilePath+'/'+fileName)
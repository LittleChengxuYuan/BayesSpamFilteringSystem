from Preprocess import Preprocess
import os
testFilePath = "./Data/train-mails/spam"
testFileList = os.listdir(testFilePath)
preprocess = Preprocess("./Data/train-mails/ham","./Data/train-mails/spam","./Data/StopWords.txt")
isSpam = 0
for fileName in testFileList:
    # print(fileName)
    result = preprocess.getResult_1("SVM",testFilePath+'/'+fileName)
    if result == 0:
        isSpam = isSpam + 1
print(isSpam/len(testFileList))
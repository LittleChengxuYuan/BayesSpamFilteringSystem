import numpy as np
import pickle
import os
import jieba
from sklearn import svm
from sklearn.externals import joblib

# 根据SVM函数特性编码，针对每一篇短文获取频率最高的十五单词，将其保存在
# 整体思路：首先获取词频字典，将所有单词保存在数组中。
# 对于每一个训练文件单词词频表来说，查找该每一个单词单词是否存在表中，如果是则保存该单词的词频，将所有添加为一个单独的数组保存，
# 同时注意保留特征数组。
class MySVM:

    def train2file(self, spamDict, hamDict, spamFilePath, hamFilePath):
        newspam = sorted(spamDict.items(), key=lambda d: d[1], reverse=True)[0:int(len(spamDict) / 2)]
        newham = sorted(hamDict.items(), key=lambda d: d[1], reverse=True)[0:int(len(hamDict) / 2)]
        wordListTupe = list(set(newspam + newham))
        spamFileList = os.listdir(spamFilePath)
        hamFileList = os.listdir(hamFilePath)
        fileNum = len(spamFileList) + len(hamFileList)
        word = [[0 for k in range(len(wordListTupe))] for i in range(fileNum+1)]
        for i in range(0, len(wordListTupe)):
            word[0][i] = wordListTupe[i][0]
        k = 1  # 特征二维数组的行数，第0行为单词列表

        Eigenvalues = []
        Eigenvalues.append(-1)
        for i in range(0, len(spamFileList)):
            Eigenvalues.append(0)
            wordDict = {}
            fileName = spamFileList[i]
            file = open(spamFilePath + '/' + fileName, encoding="utf8").read()
            res_list = jieba.lcut(file)
            # 计算本文件的词频
            for j in res_list:
                if j in wordDict.keys():
                    wordDict[j] += 1
                else:
                    wordDict.setdefault(j, 1)

            for (key, value) in wordDict.items():
                # 如果单词存在在列表中，则保留其词频
                if key in word[0]:
                    index = word[0].index(key)
                    word[k][index] = value
            k = k + 1

        for i in range(0,len(hamFileList)):
            Eigenvalues.append(1)
            wordDict = {}
            fileName = hamFileList[i]
            file = open(hamFilePath+'/'+fileName,encoding="utf8").read()
            res_list = jieba.lcut(file)
            for j in res_list:
                if j in wordDict.keys():
                    wordDict[j]+=1
                else:
                    wordDict.setdefault(j,1)
            for(key,value)in wordDict.items():
                if key in word[0]:
                    index = word[0].index(key)
                    word[k][index] = value
        theword = word[0]
        del word[0]
        del Eigenvalues[0]
        array = np.array(word)
        Eigenvalues = np.array(Eigenvalues)

        print("开始训练")
        clf = svm.SVC()
        clf.fit(array, Eigenvalues)
        joblib.dump(clf, "./File/SVM_train_model.m")
        print("训练结束")

        f = open("./File/words.bin","wb")
        pickle.dump(theword,f,True)
        f.close()

    def myPredict(self,fileDict):
        clf = joblib.load("./File/SVM_train_model.m")
        words = pickle.load(open("./File/words.bin","rb"))
        test_X = [0 for k in range(len(words))]
        for (key,value) in fileDict.items():
            if key in words:
                index = words.index(key)
                test_X[index] = value
        return (clf.predict(np.array(test_X).reshape(1,-1)))[0]



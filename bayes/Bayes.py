import math
import os
class Bayes:
    __stopList = []
    __hamDict = {}
    __spamDict = {}
    __spamFileNum = 0
    __hamFileNum = 0
    def __init__(self,hamFilePath,spamFilePath,stopWordsFilePath):


        __stopList = open(stopWordsFilePath).read().split()
        self.__getWordDict(hamFilePath,self.__hamDict,__stopList)
        self.__getWordDict(spamFilePath,self.__spamDict,__stopList)
        self.__hamFileNum = len(os.listdir(hamFilePath))
        self.__spamFileNum = len(os.listdir(spamFilePath))
    
    def getResult(self,testFile):
        testDict = self.__getTestDict(testFile,self.__stopList)
        self.__getResult(testDict,self.__spamDict,self.__hamDict,self.__spamFileNum,self.__hamFileNum)
    
    #将传入的字符串分割为单词并保存在列表里，英文可直接利用正则表达式，中文则使用结巴分词
    #计算wordList中单词出现的频数，并将其保存在字典中，该方法对各形式的邮件通用
    def __getWordDict(self,filePath,wordDict,stopList):
        fileList = os.listdir(filePath)
        for fileName in fileList:
            file_object = open(filePath+'/'+fileName).read()
            res_list = list(file_object.split())
            for i in res_list:
                if i not in stopList and i.strip()!='' and i!=None:
                    if i in wordDict.keys():
                        wordDict[i]+=1
                    else:
                        wordDict.setdefault(i,1)
    
    def __getTestDict(self,file,stopList):
        wordDict = {}
        res_list = open(file).read().split()
        for i in res_list:
            if i not in stopList and i.strip()!='' and i!=None:
                if i in wordDict.keys():
                    wordDict[i]+=1
                else:
                    wordDict.setdefault(i,1)
        return wordDict
    
    def __getResult(self,testDict,spamDict,hamDict,spamFileNum,hamFileNum):
        #垃圾邮件的概率
        wordSpamProbDict = {}
        #正常邮件的概率
        wordHamProbDict = {}
        #垃圾邮件和正常邮件的概率：p(spam),p(ham)
        p_s = spamFileNum/(spamFileNum+hamFileNum)
        p_h = hamFileNum/(spamFileNum+hamFileNum)
        for word in testDict.keys():
            #分别计算p(word|spam)和p(word|ham)
            if word in spamDict.keys() and word in hamDict.keys():
                pw_s = spamDict[word]/spamFileNum
                pw_h = hamDict[word]/hamFileNum
            if word in spamDict.keys() and word not in hamDict.keys():
                pw_s = spamDict[word]/spamFileNum
                pw_h = 0.01
            if word not in spamDict.keys() and word in hamDict.keys():
                pw_s=0.01
                pw_h=hamDict[word]/hamFileNum
            if word not in spamDict.keys() and word not in hamDict.keys():
                pw_s=0.01
                pw_h=0.01
                #wordSpamProbDict.setdefault(word,0.4)
                #wordHamProbDict.setdefault(word,0.4)
            #根据贝叶斯公式p(spam|word)=(p(word|spam)*p(spam))/(p(word|sapm)*p(spam)+p(word|ham)*p(ham))计算
            ps_w = (pw_s*p_s)/(pw_s*p_s+pw_h*p_h)
            ph_w = 1-ps_w
            #判断是否已经设为0.4
            #if word not in wordHamProbDict.keys() and word not in wordSpamProbDict.keys():
            wordSpamProbDict.setdefault(word,ps_w)
            wordHamProbDict.setdefault(word,ph_w)
        
        #只取取概率影响最大的十五个单词
        newList = sorted(wordSpamProbDict.items(),key=lambda d:d[1],reverse=True)[0:15]
        newList2 = sorted(wordHamProbDict.items(),key=lambda d:d[1],reverse=True)[0:15]
        #将所取的单词概率乘在一起
        ps = 1
        ph = 1
        for word in newList:
            #数值变得极小（趋近于0，譬如小数有300位）会自动变化为0，因此先取对数再相加
            the = word[0]
            ps += math.log(wordSpamProbDict[the])
        for word in newList2:
            the = word[0]
            ph += math.log(wordHamProbDict[the])
        #如果ph-ps>0则认为是正常邮件，否则为垃圾邮件
        if(ph-ps>0):
            print("ham")
        else:
            print("spam")
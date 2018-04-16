class Bayes:
    #获取停用词表
    def getStopList(self):
        stopList = []
        for line in open(".\\stoplist.txt"):
            stopList.append(line[:len(line)-1])
        return stopList;
    #将传入的字符串分割为单词并保存在列表里，英文可直接利用正则表达式，中文则使用结巴分词
    #计算wordList中单词出现的频数，并将其保存在字典中，该方法对正常邮件和垃圾邮件通用
    def getWordList(self,content,wordDict,stopList):
        res_list = list(content.split())
        for i in res_list:
            if i not in stopList and i.strip()!='' and i!=None:
                if i in wordDict.keys():
                    wordDict[i]+=1
                else:
                    wordDict.setdefault(i,1)
    #def getTestWords(self,test):

    

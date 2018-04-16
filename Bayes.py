class Bayes:
    #将传入的字符串分割为单词并保存在列表里，英文可直接利用正则表达式，中文则使用结巴分词
    #计算wordList中单词出现的频数，并将其保存在字典中，该方法对各形式的邮件通用
    def getWordList(self,content,wordDict,stopList):
        res_list = list(content.split())
        for i in res_list:
            if i not in stopList and i.strip()!='' and i!=None:
                if i in wordDict.keys():
                    wordDict[i]+=1
                else:
                    wordDict.setdefault(i,1)
    def getTestWords(self,testDict,spamDict,hamDict,spamFilelen,hamFileLen):
        wordProbDict = {}
        for word in testDict.keys():
            if word in spamDict.keys() and word in hamDict.keys():
                pw_s = spamDict[word]/spamFilelen
                pw_h = hamDict[word]/hamFileLen
                ps_w = pw_s/(pw_s+pw_h)
                wordProbDict.setdefault(word,ps_w)
            if word in spamDict.keys() and word not in hamDict.keys():
                pw_s = spamDict[word]/spamFilelen
                pw_h = 0.01
                ps_w = pw_s/(pw_s+pw_h)
                wordProbDict.setdefault(word,ps_w) 
            if word not in spamDict.keys() and word in hamDict.keys():
                pw_s=0.01
                pw_h=hamDict[word]/hamFileLen
                ps_w=pw_s/(pw_s+pw_h) 
                wordProbDict.setdefault(word,ps_w)
            if word not in spamDict.keys() and word not in hamDict.keys():
                #若该词不在脏词词典中，概率设为0.4
                wordProbDict.setdefault(word,0.4)
        return wordProbDict
    def calBayes(self,wordList,spamDict,hamDict):
        ps_w = 1
        ps_h = 1
        for prob in wordList.values():
            ps_w*=prob
            ps_h*=(1-prob)
        p = ps_w/(ps_w+ps_h)
        print(str(ps_w)+"////"+str(ps_h))
        return p
    

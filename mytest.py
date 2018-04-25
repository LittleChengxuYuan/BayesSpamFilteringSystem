from sklearn.svm import SVC  
import numpy as np  
X= [['e','d'],
    ['g','e'],
    ['r','c'],
    ['e','e']]
y = [1,2,3,4]
  
clf = SVC()  
clf.fit(X,y)
print (clf.predict([['e','c']]))
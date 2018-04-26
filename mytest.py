from sklearn.svm import SVC  
import numpy as np  
from openpyxl import Workbook
# X= [['e','d'],
#     ['g','e'],
#     ['r','c'],
#     ['e','e']]
# y = [1,2,3,4]
  
# clf = SVC()  
# clf.fit(X,y)
# print (clf.predict([['e','c']]))

d={'你好':1,"ads":2,"gfhj金凤凰":56}
new = sorted(d.items(),key=lambda d:d[1],reverse=True)
wb = Workbook()
sheet = wb.active
for i in range(0,len(new)):
    sheet.cell(1,i+1,value=new[i][0])
wb.save("test.xlsx")
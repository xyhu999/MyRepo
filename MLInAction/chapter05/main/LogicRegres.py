#encoding=utf-8
from util import utilService
import matplotlib.pyplot as plt
from numpy import *
from chapter05.service import logRegres

dataMat,labelMat=utilService.loadData('../data/testSet.txt')
dataArray=array(dataMat)

logRegres.gradAscent(dataMat, labelMat)

n=shape(dataArray)[0]

xcord1=[];ycord1=[]
xcord2=[];ycord2=[]

for i in range(n):
    if int(labelMat[i])==1:
        xcord1.append(dataArray[i,1])
        ycord1.append(dataArray[i,2])
    else:
        xcord2.append(dataArray[i,1])
        ycord2.append(dataArray[i,2])
        
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(xcord1,ycord1,c='red')
ax.scatter(xcord2,ycord2,c='green')
plt.show()

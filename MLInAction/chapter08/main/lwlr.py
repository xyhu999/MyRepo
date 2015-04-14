from chapter08.service import regress
from numpy import *
xArr,yArr=regress.loadDataSet("../data/ex0.txt")
yHat=regress.lwlrTest(xArr, xArr, yArr, 0.05)
xMat=mat(xArr)
srtInd=xMat[:,1].argsort(0)
xSort=xMat[srtInd][:,0,:]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(xSort[:,1],yHat[srtInd])
ax.scatter(xMat[:,1],mat(yArr).T,s=2,c='red')
plt.show()


from chapter08.service import regress
from numpy import *
xArr,yArr=regress.loadDataSet("../data/ex0.txt")
ws=regress.standRegres(xArr, yArr)
xMat=mat(xArr)
yMat=mat(yArr)

import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(xMat[:,1],yMat.T[:,0])
xCopy=xMat.copy()
xCopy.sort(0)
yHat=xCopy*ws
ax.plot(xCopy[:,1],yHat)
plt.show()
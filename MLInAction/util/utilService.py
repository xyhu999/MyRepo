#encoding=utf-8
'''
Created on 2015年4月13日

@author: yuxiang.hyx
'''
def loadData(file):
    fr=open(file)
    dataMat=[]
    labelMat=[]
    for line in fr.readlines():
        curline=line.strip().split()
        dataMat.append([1.0,float(curline[0]), float(curline[1])])
        labelMat.append(int(curline[-1]))
    return dataMat,labelMat
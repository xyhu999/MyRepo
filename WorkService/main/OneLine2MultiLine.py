#coding=utf-8 
from numpy import *
fr = open('../data/oneline2multiline','r+')

#分割字符
def getSplitChars(str):
    chars=[]
    for i in str:
        if not (i>='a'and i<='z' or i>='0' and i<='9' or i=='_' or i>='A' and i<='Z' or i=='.'):
            chars.append(i)
    return set(chars)

def my_split(str): 
    splitchars=getSplitChars(str)
#    print splitchars
    for i in splitchars:
        str = str.replace(i,' ')
    list1 = str.split()
    return list1


result='\n\n运行结果如下：\n'

for line in fr.readlines():
    lines=my_split(line.strip())
    for item in lines:
        result+=item+'\n'
fr.writelines(result)
